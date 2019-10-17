import pytest
import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

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
        submit_button = browser.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        input_value = browser.find_element_by_id("input_value")
        value = int(input_value.text)
        answer = math.log(abs(12 * math.sin(value)))
        answer_field = browser.find_element_by_id("answer")
        answer_field.send_keys(str(answer))
        submit_button = browser.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        time.sleep(20)
