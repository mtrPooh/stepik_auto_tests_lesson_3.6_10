import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSiteLanguageInterface():

    def test_add_to_cart_button_is_present(self, browser):
        browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        time.sleep(30)

        try:
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
            )
            button_is_present = True
        except:
            button_is_present = False

        assert button_is_present is True, 'Add to cart button not found!'

