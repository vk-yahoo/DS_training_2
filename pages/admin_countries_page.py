from selenium.webdriver.support.wait import WebDriverWait


class AdminCountriesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
        return self

    def assert_all_zones_are_sorted(self):
        self.open()
        country_rows = self.driver.find_elements_by_css_selector('.row')
        for x in range(len(country_rows)):
            if country_rows[x].find_element_by_css_selector('td:nth-child(6)').get_attribute('textContent') != '0':
                country_rows[x].find_element_by_css_selector('td:nth-child(5) a').click()
                zones_names = self.driver.find_elements_by_css_selector('#table-zones tr td:nth-child(3)')
                zones_list = []
                for zone in range(len(zones_names) - 1):
                    zones_list.append(zones_names[zone].get_attribute('textContent'))
                zones_list_sorted = list(zones_list)
                zones_list_sorted.sort()
                for y in range(len(zones_names) - 1):
                    assert zones_list[y] == zones_list_sorted[y]
                print('\nzones_list')
                print(zones_list)
                self.driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
                country_rows = self.driver.find_elements_by_css_selector('.row')
        return True

    def get_countries_list(self):
        self.open()
        country_page_rows = self.driver.find_elements_by_css_selector('.row td:nth-child(5) a')
        countries_list = []
        for x in range(len(country_page_rows)):
            countries_list.append(country_page_rows[x].get_attribute('textContent'))
        return countries_list

    def get_zones_list(self, country_row):
        self.open()
        if country_row.find_element_by_css_selector('td:nth-child(6)').get_attribute('textContent') != '0':
            country_row.find_element_by_css_selector('td:nth-child(5) a').click()
            zones_names = self.driver.find_elements_by_css_selector('#table-zones tr td:nth-child(3)')
            zones_list = []
            for zone in range(len(zones_names) - 1):
                zones_list.append(zones_names[zone].get_attribute('textContent'))
        return zones_list

    @property
    def country_rows(self):
        return self.driver.find_elements_by_css_selector('.row')
