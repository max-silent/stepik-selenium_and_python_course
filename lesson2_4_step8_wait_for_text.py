from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# price = browser.find_element_by_id("price")
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element_by_id("book")
button.click()
value = browser.find_element_by_id("input_value")
value = int(value.text)
answer = math.log(abs(12*math.sin(value)))
answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(str(answer))
solve_button = browser.find_element_by_id("solve")
solve_button.click()

# browser.quit()