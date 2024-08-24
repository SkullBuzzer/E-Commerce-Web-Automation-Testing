""" Conftest.py basically used to create browser setup fixture to use for all test cases """

import pytest
from selenium import webdriver
from Utility_Classes.readProperties import ReadConfig

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    """ Setup method to invoke browser and open the url """
    browser = request.config.getoption("browser_name")
    url = ReadConfig.get_application_url()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get_cookies().clear()
    driver.get(url)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture
def get_user_details():
    user_info = {}
    user_data = ReadConfig.get_user_info()
    keys = ['first_name', 'last_name', 'email', 'password', 'conf_password']
    for key, val in zip(keys, user_data):
        user_info[key] = val
    return user_info
