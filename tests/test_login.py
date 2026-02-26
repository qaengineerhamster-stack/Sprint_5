from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import register_user, login, wait_page_loaded
from locators import MainPageLocators


class TestLogin:
    def test_login_from_main_button(self, driver):
        email, password = register_user(driver)

        driver.get("https://stellarburgers.education-services.ru/")
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()

        login(driver, email, password)

        # НЕ ждём place-order как условие успеха -> только assert
        assert len(driver.find_elements(*MainPageLocators.PLACE_ORDER_BUTTON)) > 0

    def test_login_from_personal_account(self, driver):
        email, password = register_user(driver)

        driver.get("https://stellarburgers.education-services.ru/")
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        login(driver, email, password)

        assert len(driver.find_elements(*MainPageLocators.PLACE_ORDER_BUTTON)) > 0