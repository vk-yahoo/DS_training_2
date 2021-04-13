# -*- coding: utf-8 -*-


def test_admin_sections(app):
    """
    Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.
    1. на странице http://localhost/litecart/admin/?app=countries&doc=countries
        а) проверить, что страны расположены в алфавитном порядке
        б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить,
        что зоны расположены в алфавитном порядке
    2. на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones зайти в каждую из стран и проверить,
    что зоны расположены в алфавитном порядке
    """
    app.login_to_admin()

    # Check countries sorting
    countries_list = app.admin_countries_page.get_countries_list()
    countries_list_sorted = list(countries_list)
    countries_list_sorted.sort()
    for x in range(len(countries_list)):
        assert countries_list[x] == countries_list_sorted[x]

    # Check zones sorting on country page
    assert app.admin_countries_page.assert_all_zones_are_sorted() is True

    # Check geo zones sorting on geo zones page
    assert app.admin_geo_zones_page.assert_geo_zones_are_sorted() is True

