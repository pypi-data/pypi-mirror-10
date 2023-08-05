# vim: fileencoding=utf-8

# Programmer friendly subprocess wrapper.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: May 23, 2015
# URL: https://executor.readthedocs.org

"""
The :mod:`executor` module
==========================

The :mod:`executor` module defines the core functionality of the ``executor``
package. If you're looking for an easy way to run external commands from Python
take a look at the :func:`execute()` function. When you need more flexibility
consider using the underlying :class:`ExternalCommand` class directly
instead.

:func:`execute()` versus :class:`ExternalCommand`
-------------------------------------------------

In :mod:`executor` 1.x the :func:`execute()` function was the only interface
for external command execution. This had several drawbacks:

- The documentation for the :func:`execute()` function was getting way too
  complex given all of the supported options and combinations.

- There was no way to execute asynchronous external commands (running in the
  background) without sidestepping the complete :mod:`executor` module and
  going straight for :class:`subprocess.Popen` (with all of the verbosity
  that you get for free with :mod:`subprocess` :-).

- There was no way to prepare an external command without starting it
  immediately, making it impossible to prepare a batch of external commands
  before starting them (whether synchronously or asynchronously).

To solve these problems :mod:`executor` 2.x introduced the
:class:`ExternalCommand` class. This explains why :func:`execute()` is now a
trivial wrapper around :class:`ExternalCommand`: It's main purpose is to be an
easy to use shortcut that preserves compatibility with the old interface.

Classes and functions
---------------------
"""

# Standard library modules.
import logging
import os
import pipes
import subprocess
import tempfile

# Modules included in our package.
from executor.writable_property import override_properties, writable_property

# We need to know whether standard input should be encoded or not. The way to
# check depends on whether we are running on Python 2.x or Python 3.x (both of
# which we want to support).
try:
    # On Python 2.x this does nothing, on Python 3.x it will raise NameError.
    unicode = unicode
except NameError:
    # Define an unambiguous alias for our intention on Python 3.x.
    unicode = str

# Semi-standard module versioning.
__version__ = '2.1'

# Initialize a logger.
logger = logging.getLogger(__name__)


def execute(*command, **options):
    """
    Execute an external command and make sure it succeeded.

    :param command: All positional arguments are passed on to the constructor
                    of :class:`ExternalCommand`.
    :param options: All keyword arguments are passed on to the constructor of
                    :class:`ExternalCommand`.
    :returns: The return value of this function depends on two options:

              =======================================  =========================================  ==================================
              Value of :attr:`~ExternalCommand.async`  Value of :attr:`~ExternalCommand.capture`  Return value
              =======================================  =========================================  ==================================
              :data:`False`                            :data:`False`                              :data:`True` if the subprocess
                                                                                                  exited with a zero status code,
                                                                                                  :data:`False` if the subprocess
                                                                                                  exited with a nonzero status code.
              :data:`False`                            :data:`True`                               :attr:`ExternalCommand.output`
              :data:`True`                             :data:`True`                               :class:`ExternalCommand` object
              :data:`True`                             :data:`False`                              :class:`ExternalCommand` object
              =======================================  =========================================  ==================================
    :raises: :exc:`ExternalCommandFailed` when the command exits with a
             nonzero exit code (unless :attr:`~ExternalCommand.capture` is
             :data:`False`).

    If :attr:`~ExternalCommand.async` is :data:`True` then :func:`execute()`
    will automatically start the external command for you using
    :func:`~ExternalCommand.start()` (but it won't wait for it to end). If you
    want to create an :class:`ExternalCommand` object instance without
    immediately starting the external command then you can use
    :class:`ExternalCommand` directly.

    **Some examples**

    By default the status code of the external command is returned as a boolean:

    >>> from executor import execute
    >>> execute('true')
    True

    If an external command exits with a nonzero status code an exception is raised,
    this makes it easy to do the right thing (never forget to check the status code
    of an external command without having to write a lot of repetitive code):

    >>> execute('false')
    Traceback (most recent call last):
      File "executor/__init__.py", line 124, in execute
        cmd.start()
      File "executor/__init__.py", line 516, in start
        self.wait()
      File "executor/__init__.py", line 541, in wait
        self.check_errors()
      File "executor/__init__.py", line 568, in check_errors
        raise ExternalCommandFailed(self)
    executor.ExternalCommandFailed: External command failed with exit code 1! (command: bash -c false)

    The exceptions raised by :func:`execute()` expose
    :attr:`~ExternalCommandFailed.command` and
    :attr:`~ExternalCommandFailed.returncode` attributes. If you know a command
    is likely to exit with a nonzero status code and you want
    :func:`execute()` to simply return a boolean you can do this instead:

    >>> execute('false', check=False)
    False
    """
    cmd = ExternalCommand(*command, **options)
    if cmd.async:
        cmd.start()
        return cmd
    else:
        cmd.start()
        cmd.wait()
        if cmd.capture:
            return cmd.output
        else:
            return cmd.returncode == 0


class ExternalCommand(object):

    """
    Programmer friendly :class:`subprocess.Popen` wrapper.

    The :class:`ExternalCommand` class wraps :class:`subprocess.Popen` to make
    it easier to do the right thing (the simplicity of :func:`os.system()` with
    the robustness of :class:`subprocess.Popen`) and to provide additional
    features (e.g. asynchronous command execution that preserves the ability to
    provide input and capture output).

    Because the :class:`ExternalCommand` class has a lot of properties and
    methods here is a summary:

    - The writable properties :attr:`async`, :attr:`capture`, :attr:`check`,
      :attr:`command`, :attr:`directory`, :attr:`encoding`,
      :attr:`environment`, :attr:`fakeroot`, :attr:`input`, :attr:`logger`,
      :attr:`silent` and :attr:`sudo` allow you to configure how the external
      command will be run (before it is started).

    - The read only properties :attr:`command_line`, :attr:`encoded_input`,
      :attr:`is_finished`, :attr:`is_running`, :attr:`output`,
      :attr:`returncode`, :attr:`stdout` and :attr:`was_started` allow you to
      inspect if and how the external command was started, what its current
      status is and what its output is.

    - The public methods :func:`start()` and :func:`wait()` enable you to start
      external commands and wait for them to finish.

    - The internal methods :func:`check_errors()`, :func:`load_output()` and
      :func:`cleanup()` are used by :func:`start()` and :func:`wait()` so
      unless you're reimplementing one of those two methods you probably don't
      need these internal methods.
    """

    def __init__(self, *command, **options):
        """
        Construct an :class:`ExternalCommand` object.

        :param command: Any positional arguments are converted to a list and
                        used to set :attr:`command`.
        :param options: Keyword arguments can be used to conveniently override
                        the default values of :attr:`async`, :attr:`capture`,
                        :attr:`check`, :attr:`directory`, :attr:`encoding`,
                        :attr:`environment`, :attr:`fakeroot`, :attr:`input`,
                        :attr:`logger`, :attr:`silent` and :attr:`sudo`. Any
                        other keyword argument will raise :exc:`TypeError` as
                        usual.

        The external command is not started until you call :func:`start()` or
        :func:`wait()`.
        """
        # Store the command and its arguments.
        self.command = list(command)
        # Use any keyword arguments to override defaults.
        override_properties(self, **options)
        # Initialize instance variables.
        self.cached_stdout = None
        self.input_file = None
        self.null_device = None
        self.output_file = None
        self.subprocess = None

    @writable_property
    def async(self):
        """
        If this option is :data:`True` (not the default) preparations are made
        to execute the external command asynchronously (in the background).
        This has several consequences:

        - Calling :func:`start()` will start the external command but will
          not block until the external command is finished, instead you are
          responsible for calling :func:`wait()` at some later point in
          time.

        - When :attr:`input` is set its value will be written to a temporary
          file and the standard input stream of the external command is
          connected to read from the temporary file.

          By using a temporary file the external command can consume its input
          as fast or slow as it pleases without needing a separate thread or
          process to "feed" the external command.

        - When :class:`capture` is :data:`True` the standard output of the
          external command is redirected to a temporary file whose contents are
          read once the external command has finished.

          By using a temporary file the external command can produce output as
          fast or slow as it pleases without needing a thread or subprocess on
          our side to consume the output in real time.
        """
        return False

    @writable_property
    def capture(self):
        """
        If this option is :data:`True` (not the default) the standard output of
        the external command is captured and made available to the caller via
        :attr:`stdout` and :attr:`output`.

        The standard error stream will not be captured but can be silenced
        using the :attr:`silent` option.
        """
        return False

    @writable_property
    def check(self):
        """
        If this option is :data:`True` (the default) and the external command
        exits with a nonzero status code :exc:`ExternalCommandFailed` will be
        raised by :func:`start()` (when :attr:`async` isn't set) or
        :func:`wait()` (when :attr:`async` is set).
        """
        return True

    @writable_property
    def command(self):
        """
        A list of strings with the command to execute.
        """
        return []

    @property
    def command_line(self):
        """
        The command line used to actually run the external command requested by
        the user (a list of strings). The command line is constructed based on
        :attr:`command` according to the following rules:

        - If :attr:`command` contains a single string it is assumed to be a
          shell command and run using ``bash -c '...'`` which means constructs
          like semicolons, ampersands and pipes can be used (and all the usual
          caveats apply :-).

        - If :attr:`fakeroot` or :attr:`sudo` is set the respective command
          name may be prefixed to the command line generated here.
        """
        command_line = list(self.command)
        if len(command_line) == 1:
            command_line = ['bash', '-c'] + command_line
        if (self.fakeroot or self.sudo) and os.getuid() != 0:
            if self.sudo:
                # Superuser privileges requested by caller.
                command_line = ['sudo'] + command_line
            elif self.fakeroot and which('fakeroot'):
                # fakeroot requested by caller and available.
                command_line = ['fakeroot'] + command_line
            else:
                # fakeroot requested by caller but not available.
                command_line = ['sudo'] + command_line
        return command_line

    @writable_property
    def directory(self):
        """
        The working directory for the external command (a string). Defaults to
        the working directory of the current process using :data:`os.curdir`.
        """
        return os.curdir

    @property
    def encoded_input(self):
        """
        The value of :attr:`input` encoded using :attr:`encoding`. This is a
        :class:`python2:str` object (in Python 2.x) or a :class:`python3:bytes`
        object (in Python 3.x).
        """
        return (self.input.encode(self.encoding)
                if isinstance(self.input, unicode)
                else self.input)

    @writable_property
    def encoding(self):
        """
        The character encoding of standard input and standard output (a string,
        defaults to UTF-8). This option is used to encode :attr:`input` and to
        decode :attr:`output`.
        """
        return 'UTF-8'

    @writable_property
    def environment(self):
        """
        A dictionary of environment variables for the external command.

        You only need to specify environment variables that differ from those
        of the current process (that is to say the environment variables of the
        current process are merged with the variables that you specify here).
        """
        return {}

    @writable_property
    def fakeroot(self):
        """
        If this option is :data:`True` (not the default) and the current
        process doesn't have `superuser privileges`_ the external command is
        run with ``fakeroot``. If the ``fakeroot`` program is not installed a
        fall back to ``sudo`` is performed.
        """
        return False

    @writable_property
    def input(self):
        """
        The input to feed to the external command on the standard input stream.

        When you provide a :func:`python2:unicode` object (in Python 2.x) or a
        :class:`python3:str` object (in Python 3.x) as input it will be encoded
        using :attr:`encoding`. To avoid the automatic conversion you can
        simply pass a :class:`python2:str` object (in Python 2.x) or a
        :class:`python3:bytes` object (in Python 3.x).

        The conversion logic is implemented in the :attr:`encoded_input`
        attribute.
        """
        return None

    @property
    def is_running(self):
        """
        :data:`True` while the external command is running, :data:`False` when
        the external command hasn't been started yet or has already finished.
        """
        return self.subprocess.poll() is None if self.subprocess else False

    @property
    def is_finished(self):
        """
        :data:`True` once the external command has been started and has since
        finished, :data:`False` when the external command hasn't been started
        yet or is still running.
        """
        return self.subprocess.poll() is not None if self.subprocess else False

    @writable_property
    def logger(self):
        """
        The :class:`logging.Logger` object to use.

        If you are using Python's :mod:`logging` module and you find it
        confusing that external command execution is logged under the
        :mod:`executor` name space instead of the name space of the application
        or library using :mod:`executor` you can set this attribute to inject
        a custom (and more appropriate) logger.
        """
        return logger

    @property
    def output(self):
        r"""
        The value of :attr:`stdout` decoded using :attr:`encoding`. This is a
        :func:`python2:unicode` object (in Python 2.x) or a
        :class:`python3:str` object (in Python 3.x).

        This is only available when :attr:`capture` is :data:`True`. If
        :attr:`capture` is not :data:`True` then :attr:`output` will be
        :data:`None`.

        After decoding any leading and trailing whitespace is stripped and if
        the resulting string doesn't contain any remaining newlines then the
        string with leading and trailing whitespace stripped will be returned,
        otherwise the decoded string is returned unchanged:

        >>> from executor import ExternalCommand
        >>> cmd = ExternalCommand('echo naïve', capture=True)
        >>> cmd.start()
        >>> cmd.output
        u'na\xefve'
        >>> cmd.stdout
        'na\xc3\xafve\n'

        This is intended to make simple things easy (:attr:`output` makes it
        easy to deal with external commands that output a single line) while
        providing an escape hatch when the default assumptions don't hold (you
        can always use :attr:`stdout` to get the raw output).
        """
        raw_output = self.stdout
        if raw_output is not None:
            text_output = raw_output.decode(self.encoding)
            stripped_output = text_output.strip()
            return stripped_output if '\n' not in stripped_output else text_output

    @property
    def returncode(self):
        """
        The return code of the external command (an integer). When the external
        command hasn't finished yet :data:`None` is returned.
        """
        return self.subprocess.poll() if self.subprocess else None

    @writable_property
    def silent(self):
        """
        If this is :data:`True` (not the default) any output of the external
        command is silenced by redirecting the output streams to
        :data:`os.devnull`.

        You can enable :attr:`capture` and :attr:`silent` together to capture
        the standard output stream while silencing the standard error stream.
        """
        return False

    @property
    def stdout(self):
        """
        The output of the external command on its standard output stream, a
        :class:`python2:str` object (in Python 2.x) or a :class:`python3:bytes`
        object (in Python 3.x).

        This is only available when :attr:`capture` is :data:`True`. If
        :attr:`capture` is not :data:`True` then :attr:`stdout` will be
        :data:`None`.
        """
        # External command output can only be read when output capturing was enabled.
        if self.capture:
            # When running an external command asynchronously its output is
            # captured in a temporary file, which we'll read to get the output.
            self.load_output()
        return self.cached_stdout

    @writable_property
    def sudo(self):
        """
        If this option is :data:`True` (not the default) and the current
        process doesn't have `superuser privileges`_ the external command is
        run with ``sudo`` to ensure that the external command runs with
        superuser privileges.

        .. _superuser privileges: http://en.wikipedia.org/wiki/Superuser#Unix_and_Unix-like
        """
        return False

    @property
    def was_started(self):
        """
        :data:`True` once :func:`start()` has been called to start executing
        the external command, :data:`False` when :func:`start()` hasn't been
        called yet.
        """
        return self.subprocess is not None

    def start(self):
        """
        Start execution of the external command.

        :raises: :exc:`ExternalCommandFailed` when :attr:`~ExternalCommand.check` is
                 :data:`True`, :attr:`async` is :data:`False` and the external
                 command exits with a nonzero status code.

        This method instantiates a :class:`subprocess.Popen` object based on
        the defaults defined by :class:`ExternalCommand` and the overrides
        configured by the caller. What happens then depends on :attr:`async`:

        - If :attr:`async` is set :func:`start()` starts the external command
          but doesn't wait for it to end (use :func:`wait()` for that).

        - If :attr:`async` isn't set :func:`subprocess.Popen.communicate()` is
          used to synchronously execute the external command.
        """
        # Prepare the keyword arguments to subprocess.Popen().
        kw = dict(args=self.command_line,
                  cwd=self.directory,
                  env=os.environ.copy())
        kw['env'].update(self.environment)
        # Prepare the input.
        if self.input is not None:
            if self.async:
                fd, self.input_file = tempfile.mkstemp(prefix='executor-', suffix='-input.txt')
                self.logger.debug("Writing external command input to temporary file %s ..", self.input_file)
                with open(self.input_file, 'wb') as handle:
                    handle.write(self.encoded_input)
                kw['stdin'] = fd
            else:
                kw['stdin'] = subprocess.PIPE
        # Silence the standard output and error streams?
        if self.silent:
            if self.null_device is None:
                self.null_device = open(os.devnull, 'wb')
            kw['stdout'] = self.null_device
            kw['stderr'] = self.null_device
        # Prepare to capture the output.
        if self.capture:
            if self.async:
                fd, self.output_file = tempfile.mkstemp(prefix='executor-', suffix='-output.txt')
                logger.debug("Capturing external command output in temporary file %s ..", self.output_file)
                kw['stdout'] = fd
            else:
                kw['stdout'] = subprocess.PIPE
        # Construct the subprocess object.
        self.logger.debug("Executing external command: %s", quote(kw['args']))
        self.subprocess = subprocess.Popen(**kw)
        # Synchronously wait for the external command to end?
        if not self.async:
            # Feed the external command its input, capture the external
            # command's output, cleanup resources and check for errors.
            self.cached_stdout, stderr = self.subprocess.communicate(input=self.encoded_input)
            self.wait()

    def wait(self):
        """
        Wait for the external command to finish.

        :raises: :exc:`ExternalCommandFailed` when :attr:`check` is
                 :data:`True`, :attr:`async` is :data:`True` and the external
                 command exits with a nonzero status code.

        The :func:`wait()` function is only useful when :attr:`async` is
        :data:`True`, it performs the following steps:

        1. If :attr:`was_started` is :data:`False` :func:`start()` is called.
        2. If :attr:`is_finished` is :data:`False` :func:`subprocess.Popen.wait()`
           is called to wait for the external command to end.
        3. :func:`load_output()` is called (in case the caller enabled output
           capturing).
        4. :func:`cleanup()` is called to clean up temporary resources after
           the external command has ended.
        5. Finally :func:`check_errors()` is called (in case the caller
           didn't disable :attr:`check`).
        """
        if not self.was_started:
            self.start()
        if not self.is_finished:
            self.subprocess.wait()
        self.load_output()
        self.cleanup()
        self.check_errors()

    def load_output(self):
        """
        Reads the contents of the temporary file created by :func:`start()`
        (when :attr:`async` and :attr:`capture` are both set) into memory so
        that the output doesn't get lost when the temporary file is cleaned up
        by :func:`cleanup()`.
        """
        if self.output_file and os.path.isfile(self.output_file):
            with open(self.output_file, 'rb') as handle:
                self.cached_stdout = handle.read()

    def cleanup(self):
        """
        Clean up temporary resources after the external command has ended.

        This internal method is used by :func:`start()` and :func:`wait()` to
        clean up the temporary files that store the external command's input
        and output and to close the file handle to :data:`os.devnull`.
        """
        for attribute in ('input_file', 'output_file'):
            filename = getattr(self, attribute)
            if filename and os.path.isfile(filename):
                os.unlink(filename)
            setattr(self, attribute, None)
        if self.null_device:
            self.null_device.close()
            self.null_device = None

    def check_errors(self):
        """
        Raise :exc:`ExternalCommandFailed` when :attr:`check` is set and the
        external command ended with a nonzero exit code.

        This internal method is used by :func:`start()` and :func:`wait()` to
        make sure that failing external commands don't go unnoticed.
        """
        if self.check and self.returncode != 0:
            raise ExternalCommandFailed(self)

    def __repr__(self):
        """
        Report a user friendly representation of a :class:`ExternalCommand` object.
        """
        fields = [
            "async=%r" % self.async,
            "capture=%r" % self.capture,
            "check=%r" % self.check,
            "command=%r" % self.command,
            "encoding=%r" % self.encoding,
            "is_finished=%r" % self.is_finished,
            "is_running=%r" % self.is_running,
            "was_started=%r" % self.was_started,
        ]
        # The following fields are only included when they're useful.
        if self.command_line != self.command:
            fields.append("command_line=%r" % self.command_line)
        if self.directory != os.curdir:
            fields.append("directory=%r" % self.directory)
        if self.environment:
            fields.append("environment=%r" % self.environment)
        if self.fakeroot:
            fields.append("fakeroot=%r" % self.fakeroot)
        if self.input:
            fields.append("input=%r" % self.input)
        if self.output:
            fields.append("output=%r" % self.output)
        if self.returncode is not None:
            fields.append("returncode=%r" % self.returncode)
        if self.silent:
            fields.append("silent=%r" % self.silent)
        if self.sudo:
            fields.append("sudo=%r" % self.sudo)
        return "%s(%s)" % (self.__class__.__name__, ", ".join(sorted(fields)))


def quote(*args):
    """
    Quote a string or a sequence of strings to be used as command line argument(s).

    This function is a simple wrapper around :func:`pipes.quote()` which
    adds support for quoting sequences of strings (lists and tuples). For
    example the following calls are all equivalent::

      >>> from executor import quote
      >>> quote('echo', 'argument with spaces')
      "echo 'argument with spaces'"
      >>> quote(['echo', 'argument with spaces'])
      "echo 'argument with spaces'"
      >>> quote(('echo', 'argument with spaces'))
      "echo 'argument with spaces'"

    :param args: One or more strings, tuples and/or lists of strings to be quoted.
    :returns: A string containing quoted command line arguments.
    """
    if len(args) > 1:
        value = args
    else:
        value = args[0]
        if not isinstance(value, (list, tuple)):
            return pipes.quote(value)
    return ' '.join(map(quote, value))


def which(program):
    """
    Find the pathname(s) of a program on the executable search path (``$PATH``).

    :param program: The name of the program (a string).
    :returns: A list of pathnames (strings) with found programs.

    Some examples:

    >>> from executor import which
    >>> which('python')
    ['/home/peter/.virtualenvs/executor/bin/python', '/usr/bin/python']
    >>> which('vim')
    ['/usr/bin/vim']
    >>> which('non-existing-program')
    []

    """
    matches = []
    for directory in os.environ['PATH'].split(':'):
        pathname = os.path.join(directory, program)
        if os.access(pathname, os.X_OK):
            matches.append(pathname)
    return matches


class ExternalCommandFailed(Exception):

    """
    Raised by :func:`execute()`, :func:`~ExternalCommand.start()` and
    :func:`~ExternalCommand.wait()` when an external command exits with a
    nonzero status code. Exposes the following attributes:

    .. attribute:: command

       The :class:`ExternalCommand` object.

    .. attribute:: returncode

       The return code of the external command (an integer).
    """

    def __init__(self, command):
        self.command = command
        self.returncode = command.returncode
        error_message = "External command failed with exit code %s! (command: %s)"
        super(ExternalCommandFailed, self).__init__(error_message % (command.returncode, quote(command.command_line)))
