# -*- coding: utf-8 -*-


def test_admin_sections(app):
    """
    Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
    1) входит в панель администратора http://localhost/litecart/admin
    2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
    3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
    """
    app.login_to_admin()
    assert app.check_admin_sections_headers()


def test_check_product_stickers(app):
    """
    Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
    Стикеры -- это полоски в левом верхнем углу изображения товара,
    на которых написано New или Sale или что-нибудь другое.
    Сценарий должен проверять, что у каждого товара имеется ровно один стикер. (в реальности - нет :))
    """
    app.open_application()
    assert app.return_max_stickers_number() == 1
