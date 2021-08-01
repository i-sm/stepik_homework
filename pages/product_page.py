from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators
from selenium import webdriver


class ProductPage(BasePage):
    def should_be_params_in_link(self):
        assert "?promo=" in str(self.browser.current_url), "Promo code is wrong or not presented"

    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def check_bookname(self):
        text_of_allert_product_name = self.browser.find_element(*ProductPageLocators.ALLERT_PRODUCT_NAME).text
        text_of_product_name_on_page = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_NAME).text
        assert text_of_allert_product_name == text_of_product_name_on_page, "Book name doesn't matcg"

    def check_price(self):
        text_allert_price = self.browser.find_element(*ProductPageLocators.ALLERT_PRICE).text
        text_page_price = self.browser.find_element(*ProductPageLocators.PAGE_PRICE).text
        assert text_allert_price == text_page_price, "Price doesn't match"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"




