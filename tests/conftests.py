import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_test():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1400
    browser.config.window_height = 1200

    yield

    browser.quit()