from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL, wait_page_loaded
from locators import MainPageLocators


class TestConstructor:
    def test_constructor_buns_tab_active(self, driver):
        driver.get(BASE_URL)
        wait_page_loaded(driver)

        # сначала уйдём с булок, чтобы проверка была реальной
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        ).click()
        wait_page_loaded(driver)

        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")

    def test_constructor_sauces_tab_active(self, driver):
        driver.get(BASE_URL)
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()
        wait_page_loaded(driver)

        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_TAB)
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")

    def test_constructor_fillings_tab_active(self, driver):
        driver.get(BASE_URL)
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)
        ).click()
        wait_page_loaded(driver)

        fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        assert "tab_tab_type_current" in fillings_tab.get_attribute("class")