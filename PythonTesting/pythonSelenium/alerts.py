import time

from selenium import webdriver

validate_text = "Option3"

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validate_text)
# driver.find_element_by_id("alertbtn").click()
driver.find_element_by_id("confirmbtn").click()

alert = driver.switch_to.alert
print(alert.text)
assert validate_text in alert.text

time.sleep(5)

# alert.accept()
alert.dismiss() # handle cancel, no