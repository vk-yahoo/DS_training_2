# -*- coding: utf-8 -*-

import pytest
import time


def test_app_add_remove_products_to_the_cart(app):
    """
    Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
    1. Открыть главную страницу
    2. Открыть первый товар из списка
    3. Добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
    4. Подождать, пока счётчик товаров в корзине обновится
    5. Вернуться на главную страницу, повторить предыдущие шаги ещё два раза,
    6. Открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
    7. Удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
    """

    app.app_main_page.open()

    # Add products to a cart
    app.app_main_page.add_products_to_the_cart(3)
    assert app.app_main_page.get_cart_products_number() == '3'

    # Remove products from the cart
    app.app_main_page.remove_products_from_the_cart()

    app.app_main_page.open()
    assert app.app_main_page.get_cart_products_number() == '0'
