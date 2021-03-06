from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome("D:/Courses/drivers/chromedriver.exe")
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_tag_name("div").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
