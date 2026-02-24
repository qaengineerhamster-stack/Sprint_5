from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL
from locators import MainPageLocators


class TestConstructor:

    def test_constructor_buns_tab(self, driver):
        driver.get(BASE_URL)

        # сначала уйти с булок
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)
        ).click()

        # затем вернуться на булки
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        ).click()

        buns_tab = driver.find_element(*MainPageLocators.BUNS_TAB)
        assert "tab_tab_type_current" in buns_tab.get_attribute("class")