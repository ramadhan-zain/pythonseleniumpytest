import time

from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="D:\CAMPUS\PythonTestingCourse\geckodriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/")
print(f"the title of the web page: {driver.title}")
print(f"the url of the web page: {driver.current_url}")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()

driver.close() # only the current window is closed
# driver.quit() # all window