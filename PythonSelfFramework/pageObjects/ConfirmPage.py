from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ConfirmPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    country_input = (By.ID, "country")
    country_select = (By.LINK_TEXT, "Indonesia")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox']")
    submit_button = (By.CSS_SELECTOR, "[type='submit']")
    success_message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def select_country(self):
        self.driver.find_element(*ConfirmPage.country_input).send_keys("ind")
        self.wait.until(EC.presence_of_element_located((ConfirmPage.country_select))).click()

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def click_submit(self):
        self.driver.find_element(*ConfirmPage.submit_button).click()

    def get_success_message_text(self):
        return self.driver.find_element(*ConfirmPage.success_message).text

