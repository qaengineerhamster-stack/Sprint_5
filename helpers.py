from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import REGISTER_URL, LOGIN_URL
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from generators import generate_email, generate_password


def register_user(driver):
    email = generate_email()
    password = generate_password(6)

    driver.get(REGISTER_URL)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
    ).send_keys("Test")

    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Ждём ЛИБО смену URL, ЛИБО появление поля логина
    WebDriverWait(driver, 15).until(
        lambda d: "login" in d.current_url
        or len(d.find_elements(*LoginPageLocators.EMAIL_INPUT)) > 0
    )

    return email, password


def login(driver, email, password):
    driver.get(LOGIN_URL)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def assert_logged_in(driver):
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    )

    assert driver.find_element(
        *MainPageLocators.PERSONAL_ACCOUNT_LINK
    ).is_displayed()