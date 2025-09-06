import inspect
import logging
import os
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Automatically create a 'logs' directory in project root if it doesn't exist
        logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(logs_dir, exist_ok=True)

        # Log file path (platform-independent)
        log_file_path = os.path.join(logs_dir, "test_log.txt")

        # Reset logger handlers to avoid duplication or missing logs
        if logger.hasHandlers():
            logger.handlers.clear()

        # Set up file handler
        fileHandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger

    def implicitly_wait(self):
        self.driver.implicitly_wait(80)
