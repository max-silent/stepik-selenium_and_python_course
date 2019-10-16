from selenium import webdriver
import time
import unittest

#try: 
    #link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    #browser = webdriver.Chrome()
    #browser.get(link)

class UnitTests(unittest.TestCase):

  def test_unittest1(self):
    try: 
      link = "http://suninjuly.github.io/registration1.html"
      #link = "http://suninjuly.github.io/registration2.html"
      browser = webdriver.Chrome()
      browser.get(link)
      # Ваш код, который заполняет обязательные поля
      first_name_field = browser.find_element_by_css_selector(".first_block .first")
      last_name_field = browser.find_element_by_css_selector(".first_block .second")
      email_field = browser.find_element_by_css_selector(".first_block .third")

      first_name_field.send_keys("Max")
      last_name_field.send_keys("Silent")
      email_field.send_keys("fakemail@some.org")

      # Отправляем заполненную форму
      button = browser.find_element_by_css_selector("button.btn")
      button.click()

      # Проверяем, что смогли зарегистрироваться
      # ждем загрузки страницы
      time.sleep(1)

      # находим элемент, содержащий текст
      welcome_text_elt = browser.find_element_by_tag_name("h1")
      # записываем в переменную welcome_text текст из элемента welcome_text_elt
      welcome_text = welcome_text_elt.text

      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Wrong page text. Actual: '{welcome_text}'")
    finally:
      # ожидание чтобы визуально оценить результаты прохождения скрипта
      time.sleep(10)
      # закрываем браузер после всех манипуляций
      browser.quit()


  def test_unittest2(self):
    try:
      #link = "http://suninjuly.github.io/registration1.html"
      link = "http://suninjuly.github.io/registration2.html"
      browser = webdriver.Chrome()
      browser.get(link)
      # Ваш код, который заполняет обязательные поля
      first_name_field = browser.find_element_by_css_selector(".first_block .first")
      last_name_field = browser.find_element_by_css_selector(".first_block .second")
      email_field = browser.find_element_by_css_selector(".first_block .third")

      first_name_field.send_keys("Max")
      last_name_field.send_keys("Silent")
      email_field.send_keys("fakemail@some.org")

      # Отправляем заполненную форму
      button = browser.find_element_by_css_selector("button.btn")
      button.click()

      # Проверяем, что смогли зарегистрироваться
      # ждем загрузки страницы
      time.sleep(1)

      # находим элемент, содержащий текст
      welcome_text_elt = browser.find_element_by_tag_name("h1")
      # записываем в переменную welcome_text текст из элемента welcome_text_elt
      welcome_text = welcome_text_elt.text

      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Wrong page text. Actual: '{welcome_text}'")
    finally:
      # ожидание чтобы визуально оценить результаты прохождения скрипта
      time.sleep(10)
      # закрываем браузер после всех манипуляций
      browser.quit()


#finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()

if __name__=='__main__':
    unittest.main()