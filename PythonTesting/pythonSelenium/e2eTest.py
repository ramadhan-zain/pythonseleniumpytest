import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
# /div/h4/a
# //div[@class='card h-100']
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "Blackberry":
        print("blackberry found!")
        # div[2]/button
        # div/button
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']")
time.sleep(2)
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

driver.find_element_by_id("country").send_keys("ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Indonesia"))).click()
driver.find_element_by_id("checkbox2").click()
driver.find_element_by_css_selector("[type='submit']").click()

