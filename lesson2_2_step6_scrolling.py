import pytest
import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"


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
        x_value = browser.find_element_by_id("input_value")
        x_value = int(x_value.text)
        answer = calc(x_value)
        answer_field = browser.find_element_by_id("answer")
        submit_button = browser.find_element_by_css_selector("button[type='submit']")
        # browser.execute_script("return window.scrollTo(0,document.body.scrollHeight);")
        browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)

        answer_field.send_keys(answer)
        robot_checkbox = browser.find_element_by_id("robotCheckbox")
        robot_checkbox.click()
        robot_checkbox = browser.find_element_by_id("robotsRule")
        robot_checkbox.click()
        submit_button.click()
        time.sleep(20)
