from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators

BASE_URL = "https://stellarburgers.education-services.ru/"


def wait_page_loaded(driver, timeout: int = 15):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def wait_url_changed(driver, old_url: str, timeout: int = 15):
    WebDriverWait(driver, timeout).until(lambda d: d.current_url != old_url)


def register_user(driver):
    """
    Регистрирует нового пользователя и возвращает (email, password).
    """
    email = generate_email()
    password = generate_password(6)

    driver.get(f"{BASE_URL}register")
    wait_page_loaded(driver)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
    ).send_keys("Test")

    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # нейтрально ждём завершения перехода/загрузки
    wait_page_loaded(driver)

    return email, password


def login(driver, email: str, password: str):
    driver.get(f"{BASE_URL}login")
    wait_page_loaded(driver)

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # нейтрально ждём загрузки после логина
    wait_page_loaded(driver)

    # успех логина проверяем НЕ через ожидание, а через assert в тестах