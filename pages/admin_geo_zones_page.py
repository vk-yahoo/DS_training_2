from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import Select


class AdminGeoZonesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones')
        return self

    def get_countries_list(self):
        self.open()
        return self.driver.find_elements_by_css_selector('.row td:nth-child(3) a')

    def assert_geo_zones_are_sorted(self):
        countries = self.get_countries_list()
        for country in range(len(countries)):
            countries[country].click()
            zones_list = []
            zones = self.driver.find_elements_by_css_selector('#table-zones tr td:nth-child(3) select')
            for zone in range(len(zones)):
                select = Select(zones[zone])
                zones_list.append(select.first_selected_option.get_attribute("textContent"))
            zones_list_sorted = list(zones_list)
            zones_list_sorted.sort()
            for x in range(len(zones_list)):
                assert zones_list[x] == zones_list_sorted[x]
            countries = self.get_countries_list()
        return True
