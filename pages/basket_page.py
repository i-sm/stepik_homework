from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver


class BasketPage(BasePage):
    def click_show_cart(self):
        show_cart_button = self.browser.find_element(*BasePageLocators.SHOW_CART)
        show_cart_button.click()

    def check_empty_cart(self):
        text_of_allert_product_name = self.browser.find_element(*ProductPageLocators.ALLERT_PRODUCT_NAME).text
        text_of_product_name_on_page = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_NAME).text
        assert not text_of_allert_product_name == text_of_product_name_on_page, "Cart isn't empty"

    def check_empty_text(self):
       try:
           self.browser.find_element(*BasketPageLocators.EMPTY_TEXT)
           return True
       except NoSuchElementException:
           assert 1==0, "Корзина не пуста"