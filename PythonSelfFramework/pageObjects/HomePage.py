from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # * deserialize the tuple
        # driver.find_element_by_css_selector("a[href*='shop']").click()
