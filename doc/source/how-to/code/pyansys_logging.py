from copy import copy
from datetime import datetime
import logging
from logging import CRITICAL, DEBUG, ERROR, INFO, WARN
import sys

# Default configuration
LOG_LEVEL = logging.DEBUG
FILE_NAME = "PyProject.log"


# Formatting
STDOUT_MSG_FORMAT = "%(levelname)s - %(instance_name)s - %(module)s - %(funcName)s - %(message)s"
FILE_MSG_FORMAT = STDOUT_MSG_FORMAT

DEFAULT_STDOUT_HEADER = """
LEVEL - INSTANCE NAME - MODULE - FUNCTION - MESSAGE
"""
DEFAULT_FILE_HEADER = DEFAULT_STDOUT_HEADER

NEW_SESSION_HEADER = f"""
===============================================================================
       NEW SESSION - {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
==============================================================================="""

string_to_loglevel = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARN": WARN,
    "WARNING": WARN,
    "ERROR": ERROR,
    "CRITICAL": CRITICAL,
}


class InstanceCustomAdapter(logging.LoggerAdapter):
    """Keeps the reference to a product instance name dynamic.

    If you use the standard approach, which is supplying ``extra`` input
    to the logger, you would need to keep inputting product instances
    every time a log is created.

    Using adapters, you just need to specify the product instance that you refer
    to once.
    """

    # level is kept for compatibility with ``suppress_logging``,
    # but it does nothing.
    level = None
    file_handler = None
    stdout_handler = None

    def __init__(self, logger, extra=None):
        self.logger = logger
        self.extra = extra
        self.file_handler = logger.file_handler
        self.std_out_handler = logger.std_out_handler

    def process(self, msg, kwargs):
        kwargs["extra"] = {}
        # These are the extra parameters sent to log
        # here self.extra is the argument pass to the log records.
        kwargs["extra"]["instance_name"] = self.extra.get_name()
        return msg, kwargs

    def log_to_file(self, filename=FILE_NAME, level=LOG_LEVEL):
        """Add file handler to logger.

        Parameters
        ----------
        filename : str, optional
            Name of the file where the logs are recorded. By default
            ``PyProject.log``
        level : str, optional
            Level of logging, for example ``'DEBUG'``. By default
            ``logging.DEBUG``.
        """
        self.logger = add_file_handler(
            self.logger, filename=filename, level=level, write_headers=True
        )
        self.file_handler = self.logger.file_handler

    def log_to_stdout(self, level=LOG_LEVEL):
        """Add standard output handler to the logger.

        Parameters
        ----------
        level : str, optional
            Level of logging record. By default ``logging.DEBUG``.
        """
        if self.std_out_handler:
            raise Exception("Stdout logger already defined.")

        self.logger = add_stdout_handler(self.logger, level=level)
        self.std_out_handler = self.logger.std_out_handler

    def setLevel(self, level="DEBUG"):
        """Change the log level of the object and the attached handlers."""
        self.logger.setLevel(level)
        for each_handler in self.logger.handlers:
            each_handler.setLevel(level)
        self.level = level


class PyAnsysPercentStyle(logging.PercentStyle):
    def __init__(self, fmt, *, defaults=None):
        self._fmt = fmt or self.default_format
        self._defaults = defaults

    def _format(self, record):
        defaults = self._defaults
        if defaults:
            values = defaults | record.__dict__
        else:
            values = record.__dict__

        # Here you can make any changes that you want in the record. For
        # example, adding a key.

        # You could create an ``if`` here if you want conditional formatting, and even
        # change the record.__dict__.
        # If you don't want to create conditional fields, it is fine to keep
        # the same MSG_FORMAT for all of them.

        # For the case of logging exceptions to the logger.
        values.setdefault("instance_name", "")

        return STDOUT_MSG_FORMAT % values


class PyProjectFormatter(logging.Formatter):
    """Customized ``Formatter`` class used to overwrite the defaults format styles."""

    def __init__(
        self,
        fmt=STDOUT_MSG_FORMAT,
        datefmt=None,
        style="%",
        validate=True,
        defaults=None,
    ):
        if sys.version_info[1] < 8:
            super().__init__(fmt, datefmt, style)
        else:
            # 3.8: The validate parameter was added
            super().__init__(fmt, datefmt, style, validate)
        self._style = PyAnsysPercentStyle(fmt, defaults=defaults)  # overwriting


class InstanceFilter(logging.Filter):
    """Ensures that instance_name record always exists."""

    def filter(self, record):
        if not hasattr(record, "instance_name"):
            record.instance_name = ""
        return True


class Logger:
    """Logger used for each PyProject session.

    This class lets you add a handler to a file or standard output.

    Parameters
    ----------
    level : int, optional
        Logging level to filter the message severity allowed in the logger.
        The default is ``logging.DEBUG``.
    to_file : bool, optional
        Write log messages to a file. The default is ``False``.
    to_stdout : bool, optional
        Write log messages into the standard output. The
        default is ``True``.
    filename : str, optional
        Name of the file where log messages are written to.
        The default is ``None``.
    """

    file_handler = None
    std_out_handler = None
    _level = logging.DEBUG
    _instances = {}

    def __init__(
        self,
        level=logging.DEBUG,
        to_file=False,
        to_stdout=True,
        filename=FILE_NAME,
        cleanup=True,
    ):
        """Initialize Logger class."""
        self.logger = logging.getLogger("pyproject_global")  # Creating default main logger.
        self.logger.addFilter(InstanceFilter())
        self.logger.setLevel(level)
        self.logger.propagate = True
        self.level = self.logger.level  # TODO: TO REMOVE

        # Writing logging methods.
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical
        self.log = self.logger.log

        if to_file or filename != FILE_NAME:
            # We record to file.
            self.log_to_file(filename=filename, level=level)

        if to_stdout:
            self.log_to_stdout(level=level)

        self.add_handling_uncaught_expections(
            self.logger
        )  # Using logger to record unhandled exceptions.

        self.cleanup = cleanup

    def log_to_file(self, filename=FILE_NAME, level=LOG_LEVEL):
        """Add file handler to logger.

        Parameters
        ----------
        filename : str, optional
            Name of the file where the logs are recorded. By default FILE_NAME
        level : str, optional
            Level of logging. E.x. 'DEBUG'. By default LOG_LEVEL
        """
        self = add_file_handler(self, filename=filename, level=level, write_headers=True)

    def log_to_stdout(self, level=LOG_LEVEL):
        """Add standard output handler to the logger.

        Parameters
        ----------
        level : str, optional
            Level of logging record. By default LOG_LEVEL
        """
        self = add_stdout_handler(self, level=level)

    def setLevel(self, level="DEBUG"):
        """Change the log level of the object and the attached handlers."""
        self.logger.setLevel(level)
        for each_handler in self.logger.handlers:
            each_handler.setLevel(level)
        self._level = level

    def _make_child_logger(self, suffix, level):
        """Create a child logger.

        Create a child logger either using ``getChild`` or copying
        attributes between ``pyproject_global`` logger and the new
        one.

        """
        logger = logging.getLogger(suffix)
        logger.std_out_handler = None
        logger.file_handler = None

        if self.logger.hasHandlers:
            for each_handler in self.logger.handlers:
                new_handler = copy(each_handler)

                if each_handler == self.file_handler:
                    logger.file_handler = new_handler
                elif each_handler == self.std_out_handler:
                    logger.std_out_handler = new_handler

                if level:
                    # The logger handlers are copied and changed the
                    # loglevel if the specified log level is lower
                    # than the one of the global.
                    if each_handler.level > string_to_loglevel[level.upper()]:
                        new_handler.setLevel(level)

                logger.addHandler(new_handler)

        if level:
            if isinstance(level, str):
                level = string_to_loglevel[level.upper()]
            logger.setLevel(level)

        else:
            logger.setLevel(self.logger.level)

        logger.propagate = True
        return logger

    def add_child_logger(self, suffix, level=None):
        """Add a child logger to the main logger.

        This logger is more general than an instance logger which is designed
        to track the state of the application instances.

        If the logging level is in the arguments, a new logger with a
        reference to the ``_global`` logger handlers is created
        instead of a child.

        Parameters
        ----------
        suffix : str
            Name of the logger.
        level : str
            Level of logging

        Returns
        -------
        logging.logger
            Logger class.
        """
        name = self.logger.name + "." + suffix
        self._instances[name] = self._make_child_logger(self, name, level)
        return self._instances[name]

    def _add_product_instance_logger(self, name, product_instance, level):
        if isinstance(name, str):
            instance_logger = InstanceCustomAdapter(
                self._make_child_logger(name, level), product_instance
            )
        elif isinstance(name, None):
            instance_logger = InstanceCustomAdapter(
                self._make_child_logger("NO_NAMED_YET", level), product_instance
            )
        else:
            raise TypeError(f"``name`` parameter must be a string or None, not f{type(name)}")

        return instance_logger

    def add_instance_logger(self, name, product_instance, level=None):
        """Create a logger for an application instance.

        This instance logger is a logger with an adapter which add the
        contextual information such as <product/service> instance
        name. This logger is returned and you can use it to log events
        as a normal logger. It is also stored in the ``_instances``
        attribute.

        Parameters
        ----------
        name : str
            Name for the new logger
        product_instance : ansys.product.service.module.ProductClass
            Class instance. This must contain the attribute ``name``.

        Returns
        -------
        InstanceCustomAdapter
            Logger adapter customized to add additional information to
            the logs. You can use this class to log events in the
            same way you would with a logger class.

        Raises
        ------
        TypeError
            You can only input strings as ``name`` to this method.
        """
        count_ = 0
        new_name = name
        while new_name in logging.root.manager.__dict__.keys():
            count_ += 1
            new_name = name + "_" + str(count_)

        self._instances[new_name] = self._add_product_instance_logger(
            new_name, product_instance, level
        )
        return self._instances[new_name]

    def __getitem__(self, key):
        if key in self._instances.keys():
            return self._instances[key]
        else:
            raise KeyError(f"There are no instances with name {key}")

    def add_handling_uncaught_expections(self, logger):
        """Redirect the output of an exception to the logger."""

        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

        sys.excepthook = handle_exception

    def __del__(self):
        """Close the logger and all its handlers."""
        self.logger.debug("Collecting logger")
        if self.cleanup:
            try:
                for handler in self.logger.handlers:
                    handler.close()
                    self.logger.removeHandler(handler)
            except Exception:
                try:
                    if self.logger is not None:
                        self.logger.error("The logger was not deleted properly.")
                except Exception:
                    pass
        else:
            self.logger.debug("Collecting but not exiting due to 'cleanup = False'")


def add_file_handler(logger, filename=FILE_NAME, level=LOG_LEVEL, write_headers=False):
    """Add a file handler to the input.

    Parameters
    ----------
    logger : logging.Logger or logging.Logger
        Logger where to add the file handler.
    filename : str, optional
        Name of the output file. By default FILE_NAME
    level : str, optional
        Level of log recording. By default LOG_LEVEL
    write_headers : bool, optional
        Record the headers to the file. By default ``False``.

    Returns
    -------
    logger
        Return the logger or Logger object.
    """
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(FILE_MSG_FORMAT))

    if isinstance(logger, Logger):
        logger.file_handler = file_handler
        logger.logger.addHandler(file_handler)

    elif isinstance(logger, logging.Logger):
        logger.file_handler = file_handler
        logger.addHandler(file_handler)

    if write_headers:
        file_handler.stream.write(NEW_SESSION_HEADER)
        file_handler.stream.write(DEFAULT_FILE_HEADER)

    return logger


def add_stdout_handler(logger, level=LOG_LEVEL, write_headers=False):
    """Add a stream handler to the logger.

    Parameters
    ----------
    logger : logging.Logger or logging.Logger
        Logger where to add the stream handler.
    level : str, optional
        Level of log recording. By default ``logging.DEBUG``.
    write_headers : bool, optional
        Record the headers to the stream. By default ``False``.

    Returns
    -------
    logger
        The logger or Logger object.
    """
    std_out_handler = logging.StreamHandler(sys.stdout)
    std_out_handler.setLevel(level)
    std_out_handler.setFormatter(PyProjectFormatter(STDOUT_MSG_FORMAT))

    if isinstance(logger, Logger):
        logger.std_out_handler = std_out_handler
        logger.logger.addHandler(std_out_handler)

    elif isinstance(logger, logging.Logger):
        logger.addHandler(std_out_handler)

    if write_headers:
        std_out_handler.stream.write(DEFAULT_STDOUT_HEADER)

    return logger
