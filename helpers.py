
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators


BASE_URL = "https://stellarburgers.education-services.ru/"


def open_page(driver, path: str = ""):
    driver.get(f"{BASE_URL}{path}")


def register_user(driver):
    """Регистрирует нового пользователя и возвращает (email, password)."""
    email = generate_email()
    password = generate_password(6)

    open_page(driver, "register")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
    ).send_keys("Test")

    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Ждём появления страницы логина: либо URL содержит login, либо есть кнопка "Войти"
    WebDriverWait(driver, 15).until(
        lambda d: ("login" in d.current_url)
        or (len(d.find_elements(*LoginPageLocators.LOGIN_BUTTON)) > 0)
    )

    return email, password


def login(driver, email: str, password: str):
    """Логинится существующим пользователем."""
    open_page(driver, "login")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def assert_logged_in(driver):
    """Проверка успешного логина (появилась кнопка Оформить заказ)."""
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
    )
    assert len(driver.find_elements(*MainPageLocators.PLACE_ORDER_BUTTON)) > 0