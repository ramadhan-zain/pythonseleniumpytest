from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radio_button = driver.find_elements_by_name("radioButton")
radio_button[2].click()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()


driver.close()