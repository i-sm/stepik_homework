from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.browser.current_url), "Wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        input_e_mail_reg = self.browser.find_element(*LoginPageLocators.E_MAIL_REGISTERED)
        input_e_mail_reg.send_keys(email)
        input_password1_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_1_REGISTERED)
        input_password1_reg.send_keys(password)
        input_password2_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_2_REGISTERED)
        input_password2_reg.send_keys(password)
        reg_bttn = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTERED)
        reg_bttn.click()

    def should_be_registered_user(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_LINK), "Not log in"
