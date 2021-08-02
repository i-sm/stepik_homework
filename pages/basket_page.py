from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def click_show_cart(self):
        show_cart_button = self.browser.find_element(
            *BasePageLocators.SHOW_CART)
        show_cart_button.click()

    def check_empty_cart(self):
        text_of_allert_product_name = self.browser.find_element(
            *ProductPageLocators.ALLERT_PRODUCT_NAME).text
        text_of_product_name_on_page = self.browser.find_element(
            *ProductPageLocators.PAGE_PRODUCT_NAME).text
        assert not text_of_allert_product_name ==\
            text_of_product_name_on_page, "Cart isn't empty"

    def check_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT),\
            "Корзина не пуста"
