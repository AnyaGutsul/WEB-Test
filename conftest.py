import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture(scope='function')
def browser() -> WebDriver:
    driver = webdriver.Remote(
        command_executor='http://selenium__standalone-chrome:4444/wd/hub',
        options=Options())
    return driver
