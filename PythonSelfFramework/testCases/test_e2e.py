import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.get_logger()
        driver = self.driver
        wait = self.wait
        home_page = HomePage(driver, wait)
        checkout_page = home_page.shop_items()
        # driver.find_element_by_css_selector("a[href*='shop']").click()

        # checkoutPage = CheckoutPage(driver)
        log.info("getting all the card titles")
        products = checkout_page.get_card_title()
        # products = driver.find_elements_by_xpath("//div[@class='card h-100']")
        # /div/h4/a
        # //div[@class='card h-100']
        for product in products:
            # product_name = checkout_page.get_productname_text()
            product_name = product.find_element_by_xpath("div/h4/a").text
            log.info(product_name)
            if product_name == "Blackberry":
                print("blackberry found!")
                # div[2]/button
                # div/button
                product.find_element_by_xpath("div/button").click()

        checkout_page.click_checkout()
        # driver.find_element_by_css_selector("a[class*='btn-primary']")

        # driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        # wait.until(EC.presence_of_element_located(
        #     (By.XPATH, "//a[@class='nav-link btn btn-primary']"))).click()
        # driver.find_element_by_css_selector("button[class='btn btn-success']").click()
        # driver.get_screenshot_as_file("screenshot.png")

        confirm_page = checkout_page.click_checkout_final()

        # driver.find_element_by_id("country").send_keys("ind")
        # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Indonesia"))).click()
        log.info("selecting country name as Indonesia")
        confirm_page.select_country()
        # driver.find_element_by_css_selector("div[class*='checkbox']").click()
        confirm_page.get_checkbox().click()
        # driver.find_element_by_css_selector("[type='submit']").click()
        confirm_page.click_submit()

        success_message = confirm_page.get_success_message_text()
        log.info(f"success message received is {success_message}")
        print(success_message)

        assert "Success! Thank you!" in success_message

        driver.get_screenshot_as_file("screenshot.png")


