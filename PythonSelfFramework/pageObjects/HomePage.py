from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.XPATH, "//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver, self.wait)
        return checkoutPage
        # * deserialize the tuple
        # driver.find_element_by_css_selector("a[href*='shop']").click()

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)
