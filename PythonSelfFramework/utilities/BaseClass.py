import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # catches file name

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: <%(name)s> : %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object into it

        logger.setLevel(logging.INFO)
        # logger.debug("a debug statement is executed")
        # logger.info("Information statement")  # not related to errors
        # logger.warning("Something is in warning mode")
        # logger.error("A major error has happened")
        # logger.critical("Critical issue")

        return logger

