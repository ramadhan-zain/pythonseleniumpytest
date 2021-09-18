import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
# action.context_click(driver.find_element_by_id("double-click")).perform()     # right click

alert = driver.switch_to.alert
print(alert.text)
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

driver.close()