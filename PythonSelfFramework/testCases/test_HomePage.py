from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self):
        driver = self.driver

        homepage = HomePage(driver)
        # driver.find_element_by_name("name").send_keys("Name sent by automation")
        homepage.get_name().send_keys("njen")
        # driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys(
        #     "email typed by automation")
        homepage.get_email().send_keys("mail@mail.com")
        driver.find_element_by_id("exampleCheck1").click()
        dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_index(0)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        success_alert = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
        print(success_alert)

        assert "success" in success_alert

