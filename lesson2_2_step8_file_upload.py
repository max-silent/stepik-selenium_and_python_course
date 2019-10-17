import pytest
import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

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
        firstname_field = browser.find_element_by_name("firstname")
        firstname_field.send_keys("Somename")
        lastname_field = browser.find_element_by_name("lastname")
        lastname_field.send_keys("Somelastname")
        email_field = browser.find_element_by_name("email")
        email_field.send_keys("Someemail@fakemail.com")
        upload_button = browser.find_element_by_id("file")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'lesson2_2_step8_file.txt')
        upload_button.send_keys(file_path)
        submit_button = browser.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        time.sleep(20)
