# implicit wait
# explicit wait
# pause the test for few second using Time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

products_list = []

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)

products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(f"Total products displayed: {len(products)}")
assert len(products) == 3

add_to_cart_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4
for button in add_to_cart_buttons:
    products_list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(products_list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

time.sleep(2)

products_list_checkout = []
veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    products_list_checkout.append(veg.text)

print(products_list_checkout)
assert products_list == products_list_checkout
# driver.implicitly_wait(5)
# wait until 5 seconds if object is not displayed
# global wait
# 1.5 second to reach next page it will immediately resume the process
# if object do not showed up at all the max time for the test waits for 5 seconds
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
original_amount = driver.find_element_by_css_selector(".discountAmt").text
print(f"original amount: {original_amount}")

driver.find_element_by_css_selector("button.promoBtn").click()
promo_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))).text
discount_amount = driver.find_element_by_css_selector(".discountAmt").text
print(f"discount amount: {discount_amount}")
print(promo_info)

assert float(discount_amount) < float(original_amount)

sum_amount = 0
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
    sum_amount += int(amount.text)
print(sum_amount)

total_amount = driver.find_element_by_css_selector(".totAmt").text
assert sum_amount == int(total_amount)

driver.close()