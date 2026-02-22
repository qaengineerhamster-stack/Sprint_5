from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordLocators,
)
from tests.generators import generate_email, generate_password


def register_user(driver, base_url):
    # Регистрация нового пользователя для автономности тестов
    driver.get(base_url)
    driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

    email = generate_email("test", "testov", 1999)
    password = generate_password(8)

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys("Test")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
    return email, password


def login(driver, email, password):
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def assert_logged_in(driver):
    # Самый надёжный чек логина: после авторизации обычно появляется «Оформить заказ»
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))


def test_login_from_main_button(driver, base_url):
    email, password = register_user(driver, base_url)
    login(driver, email, password)
    assert_logged_in(driver)


def test_login_from_personal_account(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(base_url)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

    login(driver, email, password)
    assert_logged_in(driver)


def test_login_from_registration_form(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(base_url)
    driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()

    login(driver, email, password)
    assert_logged_in(driver)


def test_login_from_forgot_password_form(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(base_url)
    driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(ForgotPasswordLocators.LOGIN_LINK)).click()

    login(driver, email, password)
    assert_logged_in(driver)