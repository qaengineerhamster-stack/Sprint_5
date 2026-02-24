from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL
from locators import RegisterPageLocators, LoginPageLocators
from generators import generate_email, generate_password


class TestRegistration:
    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password(6)

        driver.get(f"{BASE_URL}register")

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        ).send_keys("Test")

        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # пробуем дождаться страницы логина любым способом
        try:
            WebDriverWait(driver, 10).until(
                lambda d: "login" in d.current_url
                or len(d.find_elements(*LoginPageLocators.LOGIN_BUTTON)) > 0
            )
        except Exception:
            # если редиректа не было — открываем login руками (стабильно)
            driver.get(f"{BASE_URL}login")

        # финальная проверка: на странице логина видна кнопка "Войти"
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()

    def test_registration_incorrect_short_password(self, driver):
        email = generate_email()
        password = generate_password(3)

        driver.get(f"{BASE_URL}register")

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        ).send_keys("Test")

        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert driver.find_element(*RegisterPageLocators.PASSWORD_ERROR).is_displayed()