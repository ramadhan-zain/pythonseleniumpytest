from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:\CAMPUS\PythonTestingCourse\geckodriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# NAME
driver.find_element_by_name("name").send_keys("Name sent by automation")
# driver.find_element_by_css_selector("input[name='name']").send_keys("Name sent by automation")
# css selector
# input[name='name']

# EMAIL
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys("email typed by automation")

# select class provide the methods to handle the options in dropdown
# tag name should be select
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)             # select 0 index which is Male
# dropdown.select_by_value()


# SUBMIT BUTTON
driver.find_element_by_xpath("//input[@type='submit']").click()
#xpath
# //input[@type='submit']

# success_alert = driver.find_element_by_class_name("alert-success").text
# success_alert = driver.find_element_by_css_selector("[class*='alert-success']").text
success_alert = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
print(success_alert)

assert "success" in success_alert

driver.find_element_by_id("exampleCheck1").click()
