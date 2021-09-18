import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "Indonesia":
        country.click()
        break

selected_country = driver.find_element_by_id("autosuggest").get_attribute("value")
print(selected_country)
assert selected_country == "Indonesia"