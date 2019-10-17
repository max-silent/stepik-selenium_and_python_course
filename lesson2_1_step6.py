import pytest
import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        chest_element = browser.find_element_by_id("treasure")
        x_value = chest_element.get_attribute("valuex")
        y = calc(x_value)
        print(y)
        text_field_element = browser.find_element_by_id("answer")
        text_field_element.send_keys(str(y))
        checkbox_element = browser.find_element_by_id("robotCheckbox")
        checkbox_element.click()
        radiobutton_element = browser.find_element_by_id("robotsRule")
        radiobutton_element.click()
        submit_button = browser.find_element_by_css_selector(".btn.btn-default")
        submit_button.click()
        time.sleep(60)
