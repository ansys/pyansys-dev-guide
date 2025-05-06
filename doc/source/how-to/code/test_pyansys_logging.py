import io
import logging
from pathlib import Path
import sys
import weakref

import pyansys_logging


def test_default_logger():
    """Create a logger with default options.

    Only stdout logger must be used.
    """
    capture = CaptureStdOut()
    with capture:
        test_logger = pyansys_logging.Logger()
        test_logger.info("Test stdout")

    assert "INFO -  - test_pyansys_logging - test_default_logger - Test stdout" in capture.content
    # File handlers are not activated.
    assert Path.exists(Path.exists(Path(Path.cwd() / "PyProject.log")))


def test_level_stdout():
    """Create a logger with default options.

    Only stdout logger must be used.
    """
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
    assert (
        "DEBUG -  - test_pyansys_logging - test_level_stdout - Debug stdout with level=INFO"
        not in capture.content
    )
    assert (
        "INFO -  - test_pyansys_logging - test_level_stdout - Info stdout with level=INFO"
        in capture.content
    )
    assert (
        "WARNING -  - test_pyansys_logging - test_level_stdout - Warning stdout with level=INFO"
        in capture.content
    )
    assert (
        "ERROR -  - test_pyansys_logging - test_level_stdout - Error stdout with level=INFO"
        in capture.content
    )
    assert (
        "CRITICAL -  - test_pyansys_logging - test_level_stdout - Critical stdout with level=INFO"
        in capture.content
    )
    # level=WARNING
    assert (
        "INFO -  - test_pyansys_logging - test_level_stdout - Info stdout with level=WARNING"
        not in capture.content
    )
    assert (
        "WARNING -  - test_pyansys_logging - test_level_stdout - Warning stdout with level=WARNING"
        in capture.content
    )
    assert (
        "ERROR -  - test_pyansys_logging - test_level_stdout - Error stdout with level=WARNING"
        in capture.content
    )
    assert (
        "CRITICAL -  - test_pyansys_logging - test_level_stdout - Critical stdout with level=WARNING"  # noqa: E501
        in capture.content
    )

    # File handlers are not activated.
    assert Path.exists(Path.exists(Path(Path.cwd() / "PyProject.log")))


def test_file_handlers(tmpdir):
    """Activate a file handler different from `PyProject.log`."""
    file_logger = tmpdir.mkdir("sub").join("test_logger.txt")

    test_logger = pyansys_logging.Logger(to_file=True, filename=file_logger)
    test_logger.info("Test Misc File")

    with Path.open(file_logger, "r") as f:
        content = f.readlines()

    assert Path.exists(file_logger)  # The file handler is not the default PyProject.Log
    assert len(content) == 6
    assert "NEW SESSION" in content[2]
    assert (
        "==============================================================================="
        in content[3]
    )
    assert "LEVEL - INSTANCE NAME - MODULE - FUNCTION - MESSAGE" in content[4]
    assert "INFO -  - test_pyansys_logging - test_file_handlers - Test Misc File" in content[5]

    # Delete the logger and its file handler.
    test_logger_ref = weakref.ref(test_logger)
    del test_logger
    assert test_logger_ref() is None


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
