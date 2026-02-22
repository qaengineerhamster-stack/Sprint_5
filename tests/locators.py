from selenium.webdriver.common.by import By


class MainPageLocators:
    # Главная страница
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

    # Личный кабинет (самый стабильный вариант — по href)
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href,'/account')]")

    CONSTRUCTOR_TAB = (By.XPATH, "//*[contains(text(),'Конструктор')]")
    LOGO = (By.XPATH, "//header//a")

    # Признак успешного логина
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    # Конструктор
    BUNS_TAB = (By.XPATH, "//span[contains(.,'Булки')]/parent::*")
    SAUCES_TAB = (By.XPATH, "//span[contains(.,'Соусы')]/parent::*")
    FILLINGS_TAB = (By.XPATH, "//span[contains(.,'Начинки')]/parent::*")

    BUNS_HEADER = (By.XPATH, "//h2[contains(.,'Булки')]")
    SAUCES_HEADER = (By.XPATH, "//h2[contains(.,'Соусы')]")
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(.,'Начинки')]")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/..//input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(.,'Пароль')]/..//input")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")

    REGISTER_LINK = (By.XPATH, "//a[contains(.,'Зарегистрироваться')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(.,'Восстановить пароль')]")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(.,'Имя')]/..//input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/..//input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(.,'Пароль')]/..//input")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")

    PASSWORD_ERROR = (
        By.XPATH,
        "//*[contains(@class,'input__error') and contains(.,'Некорректный пароль')]",
    )

    LOGIN_LINK = (By.XPATH, "//a[contains(.,'Войти')]")


class ForgotPasswordLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(.,'Войти')]")


class ProfileLocators:
    # Универсальный локатор выхода
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Выход') or contains(.,'Выйти')] | "
        "//a[contains(.,'Выход') or contains(.,'Выйти')]",
    )