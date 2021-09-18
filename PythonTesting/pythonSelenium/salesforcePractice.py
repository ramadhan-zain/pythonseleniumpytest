from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\CAMPUS\PythonTestingCourse\chromedriver.exe")
driver.maximize_window()

driver.get("https://login.salesforce.com/")

# input#username
# #username
driver.find_element_by_css_selector("#username").send_keys("user_name")

driver.find_element_by_css_selector(".password").send_keys("password")
driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()

#//tagname[text()='xxx']
# //input[@value='Cancel']
driver.find_element_by_xpath("//input[@value='Cancel']").click()

#child
# //div[@id='usernamegroup']/label          xpath
# div[id='usernamegroup'] label             css

# //form[@name='login']/div[1]/label        xpath

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

# password
# form[name='login'] label:nth-child(3)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)