from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '[name="login_submit"]')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALLERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALLERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PAGE_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_CART = (By.CSS_SELECTOR, ".btn-group .btn-default")


class BasketPageLocators():
    EMPTY_TEXT = (By.CSS_SELECTOR, "[id = content_inner] p")

