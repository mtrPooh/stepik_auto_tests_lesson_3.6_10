import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSiteLanguageInterface():
    # Тест наличия кнопки добавления товара в корзину
    def test_add_to_cart_button_is_present(self, browser):
        # Открываем страницу
        browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        # Таймаут 30 сек для визуальной проверки соответствия заданного языка при запуске теста
        # и языка страницы
        time.sleep(30)

        try:
            # Ждем появления кнопки добавления товара в корзину 10 сек
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
            )

            # Флаг обнаружения кнопки добавления товара в корзину
            button_is_present = True
        except:
            # Флаг отсутствия кнопки добавления товара в корзину
            button_is_present = False

        # Проверяем наличие кнопки добавления товара в корзину
        assert button_is_present is True, 'Add to cart button not found!'

