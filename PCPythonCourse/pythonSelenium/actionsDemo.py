import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
hover_menu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(hover_menu).perform()
time.sleep(1)
child_hover_menu = driver.find_element_by_link_text("Top")
action.move_to_element(child_hover_menu).click().perform()

print(driver.current_url)