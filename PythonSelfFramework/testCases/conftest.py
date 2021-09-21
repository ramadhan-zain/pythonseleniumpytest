import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r"E:\PythonTestingCourse\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=r"E:\PythonTestingCourse\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 7)

    request.cls.driver = driver
    request.cls.wait = wait
    yield

    # driver.close()




