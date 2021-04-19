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
        zones_list = []
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

    @property
    def add_new_country_button(self):
        return self.driver.find_element_by_css_selector('a.button')

    @property
    def internal_links_on_add_new_country_page(self):
        return self.driver.find_elements_by_css_selector('#content .fa-external-link')

    def check_internal_links_on_add_new_country_page(self):
        main_window = self.driver.current_window_handle
        internal_links = self.internal_links_on_add_new_country_page
        for link in range(len(internal_links)):
            internal_links[link].click()
            available_windows = self.driver.window_handles
            if available_windows[0] == main_window:
                self.driver.switch_to.window(available_windows[1])
            else:
                self.driver.switch_to.window(available_windows[0])
            self.driver.close()
            self.driver.switch_to.window(main_window)
        print('\n ')
        print('All %s external links were opened in new window' % len(internal_links))
