from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators
from helpers import BASE_URL


class TestConstructor:
    def test_constructor_buns_tab(self, driver):
        driver.get(BASE_URL)

        # 1) Сначала уходим на Соусы (чтобы проверка перехода на Булки была честной)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()

        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")

        # 2) Переходим на Булки
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        ).click()

        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")

        # Дополнительно можно дождаться заголовка секции
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
        )