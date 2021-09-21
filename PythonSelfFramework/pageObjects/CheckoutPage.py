from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    products = (By.XPATH, "//div[@class='card h-100']")
    product_name = (By.XPATH, "div/h4/a")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_button_final = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def get_productname_text(self):
        return self.driver.find_element(*CheckoutPage.product_name).text

    def click_checkout(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()

    def click_checkout_final(self):
        return self.wait.until(EC.presence_of_element_located(*CheckoutPage.checkout_button_final))



