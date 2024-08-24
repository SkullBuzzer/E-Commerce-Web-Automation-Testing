""" This module contains custom logger function to generate more efficient logs during test execution """

import logging
import inspect

class LogGen:
    """ class with methods to generate logs """

    @staticmethod
    def get_logs():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        fileHandler = logging.FileHandler(".\\Reports_and_Logs\\Automation.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger