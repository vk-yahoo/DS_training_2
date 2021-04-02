from selenium import webdriver
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.admin_panel_main_page import AdminPanelMainPage
from pages.app_main_page import AppMainPage
from pages.customer_list_page import CustomerListPage
from pages.registration_page import RegistrationPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.registration_page = RegistrationPage(self.driver)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.admin_panel_main_page = AdminPanelMainPage(self.driver)
        self.app_main_page = AppMainPage(self.driver)
        self.customer_list_page = CustomerListPage(self.driver)

    # Admin part

    def login_to_admin(self):
        if self.admin_panel_login_page.open().is_on_this_page():
            self.admin_panel_login_page.enter_username("admin").enter_password("admin").submit_login()
        return self

    def quit(self):
        self.driver.quit()

    def register_new_customer(self, customer):
        self.registration_page.open()
        self.registration_page.firstname_input.send_keys(customer.firstname)
        self.registration_page.lastname_input.send_keys(customer.lastname)
        self.registration_page.address1_input.send_keys(customer.address)
        self.registration_page.postcode_input.send_keys(customer.postcode)
        self.registration_page.city_input.send_keys(customer.city)
        self.registration_page.select_country(customer.country)
        self.registration_page.select_zone(customer.zone)
        self.registration_page.email_input.send_keys(customer.email)
        self.registration_page.phone_input.send_keys(customer.phone)
        self.registration_page.password_input.send_keys(customer.password)
        self.registration_page.confirmed_password_input.send_keys(customer.password)
        self.registration_page.create_account_button.click()

    def get_customer_ids(self):
        self.login_to_admin()
        return self.customer_list_page.open().get_customer_ids()

    def check_admin_sections_headers(self):
        admin_sections_count = self.admin_panel_main_page.open().admin_sections_count
        self.driver.refresh()
        for x in range(admin_sections_count):
            self.admin_panel_main_page.open_section_by_index(x)
            assert self.admin_panel_main_page.section_header
            sub_sections_count = self.admin_panel_main_page.sub_sections_count(x)
            if sub_sections_count > 2:
                for y in range(2, sub_sections_count):
                    self.admin_panel_main_page.open_subsection_by_index(x, y)
                    assert self.admin_panel_main_page.section_header
        return True

    # Application part

    def open_application(self):
        return self.app_main_page.open()

    def return_max_stickers_number(self):
        counter = 0
        products_count = len(self.app_main_page.products)
        for product in range(products_count):
            if self.app_main_page.stickers_count(product) > counter:
                counter = self.app_main_page.stickers_count(product)
        return counter
