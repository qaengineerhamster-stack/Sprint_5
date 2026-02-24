from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import register_user, login, assert_logged_in, BASE_URL
from locators import MainPageLocators, ProfileLocators


class TestAccount:
    def test_open_personal_account(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)
        assert_logged_in(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ProfileLocators.LOGOUT_BUTTON)
        )

        assert len(driver.find_elements(*ProfileLocators.LOGOUT_BUTTON)) > 0

    def test_logout_from_profile(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)
        assert_logged_in(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        logout_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ProfileLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 15).until(lambda d: "login" in d.current_url)
        assert "login" in driver.current_url

    def test_from_profile_to_constructor_by_constructor_link(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)
        assert_logged_in(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB)
        ).click()

        # Надёжнее проверять по URL ИЛИ по заголовку конструктора
        WebDriverWait(driver, 15).until(
            lambda d: d.current_url.rstrip("/") == BASE_URL.rstrip("/")
            or len(d.find_elements(*MainPageLocators.BUNS_HEADER)) > 0
        )

        assert (
            driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
            or len(driver.find_elements(*MainPageLocators.BUNS_HEADER)) > 0
        )

    def test_from_profile_to_constructor_by_logo(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)
        assert_logged_in(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()

        WebDriverWait(driver, 15).until(
            lambda d: d.current_url.rstrip("/") == BASE_URL.rstrip("/")
            or len(d.find_elements(*MainPageLocators.BUNS_HEADER)) > 0
        )

        assert (
            driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
            or len(driver.find_elements(*MainPageLocators.BUNS_HEADER)) > 0
        )