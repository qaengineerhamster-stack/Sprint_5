from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, LoginPageLocators
from helpers import register_user, login, assert_logged_in, BASE_URL


class TestLogin:
    def test_login_from_main_button(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()

        login(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_personal_account(self, driver):
        email, password = register_user(driver)

        driver.get(BASE_URL)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        login(driver, email, password)
        assert_logged_in(driver)