from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("/")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s(".ActionListItem-label").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible