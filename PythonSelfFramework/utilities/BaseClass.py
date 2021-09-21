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

