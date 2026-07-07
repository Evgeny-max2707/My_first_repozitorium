from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    # Инициализируем Page Object
    page = ProductPage(browser, link)
    
    # Открываем страницу
    page.open()
    
    # Получаем название и цену товара до добавления в корзину
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Добавляем товар в корзину
    page.add_to_basket()
    
    # Проверяем сообщение об успешном добавлении
    page.should_be_success_message()
    
    # Проверяем, что название товара в сообщении правильное
    page.should_be_correct_product_name(product_name)
    
    # Проверяем, что цена корзины совпадает с ценой товара
    page.should_be_correct_basket_total(product_price)

def test_guest_can_add_product_to_basket_with_promo(browser):
    # Другая ссылка с другим промо-кодом
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
    # Инициализируем Page Object
    page = ProductPage(browser, link)
    
    # Открываем страницу
    page.open()
    
    # Получаем название и цену товара со страницы
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Добавляем товар в корзину
    page.add_to_basket()

    # Проверяем, что есть сообщение об успешном добавлении
    page.should_be_success_message()
    
    # Проверяем, что название товара в сообщении совпадает с названием на странице
    page.should_be_correct_product_name(product_name)
    
    # Проверяем, что цена корзины совпадает с ценой товара
    page.should_be_correct_basket_total(product_price)