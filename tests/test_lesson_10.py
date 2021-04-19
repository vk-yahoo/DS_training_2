# -*- coding: utf-8 -*-


def browser_logs(driver):
    logs = driver.get_log("browser")
    if logs:
        for log in logs:
            print(log)
    else:
        print('\nNo browser logs available')


def test_admin_add_product(app):
    """
    Сделайте сценарий, который проверяет, не появляются ли в логе браузера сообщения
    при открытии страниц в учебном приложении, а именно - страниц товаров в каталоге в административной панели.

    Сценарий должен состоять из следующих частей:
    1) зайти в админку
    2) открыть каталог, категорию, которая содержит товары
    (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
    3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения
    """

    # Login to the admin
    app.login_to_admin()

    # Open the Catalog page
    app.admin_catalog_page.open_products_list()

    # Open every available product page
    for i in range(2, app.admin_catalog_page.get_products_number()):
        app.admin_catalog_page.open_product_by_index(i)
        browser_logs(app. driver)
        app.admin_catalog_page.open_products_list()
