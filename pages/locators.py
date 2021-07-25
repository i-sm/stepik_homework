from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name="login_submit"]')
