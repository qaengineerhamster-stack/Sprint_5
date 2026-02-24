from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegisterPageLocators, LoginPageLocators
from generators import generate_email, generate_password
from helpers import BASE_URL


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

        # Ждём появления формы логина (или редиректа)
        WebDriverWait(driver, 15).until(
            lambda d: ("login" in d.current_url)
            or len(d.find_elements(*LoginPageLocators.LOGIN_BUTTON)) > 0
        )

        assert ("login" in driver.current_url) or (
            len(driver.find_elements(*LoginPageLocators.LOGIN_BUTTON)) > 0
        )

    def test_registration_incorrect_short_password(self, driver):
        email = generate_email()
        password = generate_password(5)  # короткий

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

        assert len(driver.find_elements(*RegisterPageLocators.PASSWORD_ERROR)) > 0