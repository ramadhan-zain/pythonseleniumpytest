from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver, self.wait)
        return checkoutPage
        # * deserialize the tuple
        # driver.find_element_by_css_selector("a[href*='shop']").click()
