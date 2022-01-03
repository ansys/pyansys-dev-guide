import io
import logging
import os
import sys
import tempfile

import pytest

sys.path.append(os.path.join("..", "logging"))
import pyansys_logging


def test_default_logger():
    """Create a logger with default options.
    Only stdout logger must be used."""

    capture = CaptureStdOut()
    with capture:
        test_logger = pyansys_logging.Logger()
        test_logger.info("Test stdout")

    assert "INFO -  - test_pyansys_logging - test_default_logger - Test stdout" in capture.content
    # File handlers are not activated.
    assert os.path.exists(os.path.exists(os.path.join(os.getcwd(), "PyProject.log")))


def test_level_stdout():
    """Create a logger with default options.
    Only stdout logger must be used."""

    capture = CaptureStdOut()
    with capture:
        test_logger = pyansys_logging.Logger(level=logging.INFO)
        test_logger.debug("Debug stdout with level=INFO")
        test_logger.info("Info stdout with level=INFO")
        test_logger.warning("Warning stdout with level=INFO")
        test_logger.error("Error stdout with level=INFO")
        test_logger.critical("Critical stdout with level=INFO")

        # Modify the level
        test_logger.setLevel(level=logging.WARNING)
        test_logger.debug("Debug stdout with level=WARNING")
        test_logger.info("Info stdout with level=WARNING")
        test_logger.warning("Warning stdout with level=WARNING")
        test_logger.error("Error stdout with level=WARNING")
        test_logger.critical("Critical stdout with level=WARNING")

    # level=INFO
    assert "DEBUG -  - test_pyansys_logging - test_level_stdout - Debug stdout with level=INFO" not in capture.content
    assert "INFO -  - test_pyansys_logging - test_level_stdout - Info stdout with level=INFO" in capture.content
    assert "WARNING -  - test_pyansys_logging - test_level_stdout - Warning stdout with level=INFO" in capture.content
    assert "ERROR -  - test_pyansys_logging - test_level_stdout - Error stdout with level=INFO" in capture.content
    assert "CRITICAL -  - test_pyansys_logging - test_level_stdout - Critical stdout with level=INFO" in capture.content
    # level=WARNING
    assert "INFO -  - test_pyansys_logging - test_level_stdout - Info stdout with level=WARNING" not in capture.content
    assert (
        "WARNING -  - test_pyansys_logging - test_level_stdout - Warning stdout with level=WARNING" in capture.content
    )
    assert "ERROR -  - test_pyansys_logging - test_level_stdout - Error stdout with level=WARNING" in capture.content
    assert (
        "CRITICAL -  - test_pyansys_logging - test_level_stdout - Critical stdout with level=WARNING" in capture.content
    )

    # File handlers are not activated.
    assert os.path.exists(os.path.exists(os.path.join(os.getcwd(), "PyProject.log")))


def test_default_file_handlers():
    """Activate the `PyProject.log` file handler."""

    current_dirctory = os.getcwd()
    file_logger = os.path.join(current_dirctory, "PyProject.log")
    if os.path.exists(file_logger):
        os.remove(file_logger)

    content = None
    test_logger = pyansys_logging.Logger(to_file=True)
    test_logger.info("Test PyProject.Log")

    with open(file_logger, "r") as f:
        content = f.readlines()

    assert len(content) == 6
    assert "NEW SESSION" in content[2]
    assert "===============================================================================" in content[3]
    assert "LEVEL - INSTANCE NAME - MODULE - FUNCTION - MESSAGE" in content[4]
    assert "INFO -  - test_pyansys_logging - test_default_file_handlers - Test PyProject.Log" in content[5]

    # Remove file's handlers and delete the file.
    for handler in test_logger.logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.close()
            test_logger.logger.removeHandler(handler)
    os.remove(file_logger)


def test_file_handlers():
    """Activate a file handler different from `PyProject.log`."""

    content = None
    current_dirctory = os.getcwd()
    file_logger = os.path.join(current_dirctory, "test_logger.txt")
    if os.path.exists(file_logger):
        os.remove(file_logger)
    test_logger = pyansys_logging.Logger(to_file=True, filename=file_logger)
    test_logger.info("Test Misc File")

    with open(file_logger, "r") as f:
        content = f.readlines()

    assert os.path.exists(file_logger)  # The file handler is not the default PyProject.Log
    assert len(content) == 6
    assert "NEW SESSION" in content[2]
    assert "===============================================================================" in content[3]
    assert "LEVEL - INSTANCE NAME - MODULE - FUNCTION - MESSAGE" in content[4]
    assert "INFO -  - test_pyansys_logging - test_file_handlers - Test Misc File" in content[5]

    # Remove file's handlers and delete the file.
    for handler in test_logger.logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.close()
            test_logger.logger.removeHandler(handler)
    os.remove(file_logger)


class CaptureStdOut:
    """Capture standard output with a context manager."""

    def __init__(self):
        self._stream = io.StringIO()

    def __enter__(self):
        sys.stdout = self._stream

    def __exit__(self, type, value, traceback):
        sys.stdout = sys.__stdout__

    @property
    def content(self):
        """Return the captured content."""
        return self._stream.getvalue()
