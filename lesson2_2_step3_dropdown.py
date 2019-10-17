import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        number_1 = browser.find_element_by_id("num1")
        number_1 = int(number_1.text)
        number_2 = browser.find_element_by_id("num2")
        number_2 = int(number_2.text)
        summed_up = number_1 + number_2
        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_value(str(summed_up))
        submit_button = browser.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        time.sleep(20)
