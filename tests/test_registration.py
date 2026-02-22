from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators
from tests.generators import generate_email, generate_password


def test_successful_registration(driver, base_url):
    driver.get(base_url)

    driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

    email = generate_email("test", "testov", 1999)
    password = generate_password(8)

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys("Test")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # после регистрации обычно перебрасывает на логин
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))


def test_registration_incorrect_short_password(driver, base_url):
    driver.get(base_url)

    driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

    email = generate_email("test", "testov", 1999)
    short_password = "12345"  # < 6

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys("Test")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))