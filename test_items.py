from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_has_a_button_add_to_basket(browser):
    browser.get(link)
    try:
	    #ожидание загрузки кнопки добавления в корзину
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
        browser.find_element_by_css_selector(".btn-add-to-basket")
        has_a_button = True
    except:
	    has_a_button = False
    assert has_a_button == True, "Button add to basket not found!"
    #команда курса в комментариях сообщает, что лучше добавить для удобства рецензирующего
    time.sleep(30)