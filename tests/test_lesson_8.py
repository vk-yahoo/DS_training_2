# -*- coding: utf-8 -*-


def test_admin_add_product(app):
    """
    Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.

    Сценарий должен состоять из следующих частей:
    1) зайти в админку
    2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
    3) открыть на редактирование какую-нибудь страну или начать создание новой
    4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой.
    Они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.

    Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
    Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
    потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.

    Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.
    """
    # Login to the admin
    app.login_to_admin()

    # Open Countries page and click on "Add New Country" button
    app.admin_countries_page.open_geo_zones_page()
    app.admin_countries_page.add_new_country_button.click()

    # Check external links
    app.admin_countries_page.check_internal_links_on_add_new_country_page()
