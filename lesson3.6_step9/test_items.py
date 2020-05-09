from selenium.webdriver.common.by import By
import time


def test_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(5)
    assert len(browser.find_elements(By.CLASS_NAME,"btn-primary"))>0, "Кнопка добавления в корзину не НАЙДЕНА"
