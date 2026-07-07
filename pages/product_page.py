from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        # Находим кнопку "Добавить в корзину" и кликаем
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        
        # Решаем математическую задачу в алерте
        self.solve_quiz_and_get_code()
    
    def should_be_success_message(self):
        # Проверяем, что есть сообщение об успешном добавлении
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"
    
    def should_be_correct_product_name(self, expected_name):
        # Получаем название товара из сообщения
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        # Проверяем, что название товара в сообщении совпадает с ожидаемым
        assert expected_name == actual_name, \
            f"Expected product name '{expected_name}' in success message, but got '{actual_name}'"
    
    def should_be_correct_basket_total(self, expected_price):
        # Получаем цену корзины из сообщения
        actual_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        # Проверяем, что цена корзины совпадает с ожидаемой
        assert expected_price == actual_price, \
            f"Expected basket total '{expected_price}', but got '{actual_price}'"
    
    def get_product_name(self):
        # Возвращает название товара со страницы
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        # Возвращает цену товара со страницы
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text