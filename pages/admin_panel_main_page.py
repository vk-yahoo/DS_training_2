from selenium.webdriver.support.wait import WebDriverWait


class AdminPanelMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/public_html/admin")
        return self

    def open_section_by_index(self, index):
        self.admin_sections[index].click()

    def open_subsection_by_index(self, section_index, subsection_index):
        self.admin_subsections(section_index)[subsection_index].click()

    @property
    def admin_sections_count(self):
        return len(self.driver.find_elements_by_css_selector('#app-'))

    def sub_sections_count(self, index):
        return len(self.find_admin_section_by_index(index).find_elements_by_css_selector('a'))

    @property
    def admin_sections(self):
        return self.driver.find_elements_by_css_selector('#app-')

    def find_admin_section_by_index(self, index):
        return self.driver.find_elements_by_css_selector('#app-')[index]

    def admin_subsections(self, section_index):
        return self.driver.find_elements_by_css_selector('#app-')[section_index].find_elements_by_css_selector('a')

    @property
    def section_header(self):
        return self.driver.find_element_by_tag_name('h1')
