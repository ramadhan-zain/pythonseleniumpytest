from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class='card h-100']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

