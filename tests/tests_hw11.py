from selene.support.shared import browser
from selene import have
import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser_test():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.window_width = 850
    browser.config.window_height = 1000


def test_selen(browser_test):
    browser.config.hold_driver_at_exit = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('olga')
    browser.element('#lastName').type('kushch')
    browser.element('.col-md-9 [id=userEmail]').type('test_qa@qmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('.col-md-9 [id=userNumber]').type(9119291972)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1996"]').click()
    browser.element('.react-datepicker__day--022').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_1.jpg'))
    browser.element('.col-md-9 [id = currentAddress]').type('SPB')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('.col-sm-12 [id=submit]').click()
    browser.element('.modal-header [id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('kushch olga'
                                               and 'test_qa@qmail.com'
                                               and 'Male'
                                               and '9119291972'
                                               and '22 Sep 1996'
                                               and 'English'
                                               and 'Sport'
                                               and 'SPB'
                                               and 'NCR Delhi'))

# коммент для коммита
# починила что ли?