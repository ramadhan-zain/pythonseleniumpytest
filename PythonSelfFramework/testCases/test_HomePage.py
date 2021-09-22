import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.get_logger()
        driver = self.driver
        wait = self.wait

        homepage = HomePage(driver, wait)

        log.info(f"first name is {get_data['first name']}")
        # driver.find_element_by_name("name").send_keys("Name sent by automation")
        homepage.get_name().send_keys(get_data["first name"])

        # driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys(
        #     "email typed by automation")
        homepage.get_email().send_keys(get_data["last name"])

        # driver.find_element_by_id("exampleCheck1").click()
        homepage.get_checkbox().click()

        self.select_option_by_text(homepage.get_gender(), get_data["gender"])

        # driver.find_element_by_xpath("//input[@type='submit']").click()
        homepage.get_submit().click()

        # success_alert = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
        success_alert = homepage.get_success_message().text

        print(success_alert)

        assert "success" in success_alert
        driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def get_data(self, request):
        return request.param
