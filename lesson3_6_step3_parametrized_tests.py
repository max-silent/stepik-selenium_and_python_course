import pytest
from selenium import webdriver
import time
import math

secret_message = ''

link_template = "https://stepik.org/lesson/{}/step/1"
urls = [link_template.format("236895"),
             link_template.format("236896"),
             link_template.format("236897"),
             link_template.format("236898"),
             link_template.format("236899"),
             link_template.format("236903"),
             link_template.format("236904"),
             link_template.format("236905")]


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
    # print("\nHidden message is: \"{}\"".format(secret_message))
    print(f"\nHidden message is: \"{secret_message}\"")


@pytest.mark.parametrize('url', urls)
def test_guest_should_see_login_link(browser, url):
    global secret_message
    browser.get(url)
    input_box = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    input_box.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    output_text = browser.find_element_by_css_selector(".attempt__message pre.smart-hints__hint")
    output_text = output_text.text
    print("\n", output_text)
    if not "Correct!" in output_text:
        secret_message += output_text
