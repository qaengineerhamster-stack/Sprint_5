from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import MainPageLocators, ProfileLocators, LoginPageLocators
from tests.test_login import register_user, login


def test_open_personal_account(driver, base_url):
    email, password = register_user(driver, base_url)
    login(driver, email, password)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(ProfileLocators.LOGOUT_BUTTON)
    )


def test_logout_from_profile(driver, base_url):
    email, password = register_user(driver, base_url)
    login(driver, email, password)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )


def test_from_profile_to_constructor_by_constructor_link(driver, base_url):
    email, password = register_user(driver, base_url)
    login(driver, email, password)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
    )


def test_from_profile_to_constructor_by_logo(driver, base_url):
    email, password = register_user(driver, base_url)
    login(driver, email, password)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.LOGO)
    ).click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
    )