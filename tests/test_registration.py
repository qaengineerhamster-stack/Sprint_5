from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from helpers import BASE_URL, wait_page_loaded
from locators import RegisterPageLocators, LoginPageLocators


class TestRegistration:
    def test_successful_registration(self, driver):
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

        wait_page_loaded(driver)

        # ассерт: что реально на странице логина
        assert len(driver.find_elements(*LoginPageLocators.LOGIN_BUTTON)) > 0

    def test_registration_incorrect_short_password(self, driver):
        email = generate_email()
        password = generate_password(5)  # короткий пароль

        driver.get(f"{BASE_URL}register")
        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT)
        ).send_keys("Test")

        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # тут НЕ надо ждать пароль-ошибку как успех? — но это и есть проверка
        # значит делаем ожидание НЕ как "успех", а как "нейтрально"? Нейтрального маркера нет.
        # поэтому здесь допустимо ждать появления ошибки и потом assert по тексту/наличию.
        error = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert error.is_displayed()