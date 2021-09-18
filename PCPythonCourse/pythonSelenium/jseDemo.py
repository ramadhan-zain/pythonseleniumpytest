# JSE DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
# print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
# in case if selenium cant click the button because intercepted another button
shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")