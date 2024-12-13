from email.policy import default

import allure

import page_objects.web_objects.main_page as main
import page_objects.web_objects.your_cart_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:
    @staticmethod
    @allure.step('Login to Swag lubs flow')
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_btn_login())

    @staticmethod
    @allure.step('verify Swag Lubs title flow')
    def verify_swag_labs_title(expected: str):
        wait(For.ELEMENT_EXISTS ,main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    # Verify Menu Buttons Using smart-assertions
    @staticmethod
    @allure.step('verify displayed menu button flow using smart assertions')
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_btn_menu(),
                 page.web_upper_menu.get_product_sort(),
                 page.web_upper_menu.get_shopping_cart()
                 ]
        Verifications.soft_assertion(elems)

    # Verify Menu Buttons Using my implementation
    @staticmethod
    @allure.step('verify displayed menu button flow using my implementation')
    def verify_menu_buttons_flow_my_implementation():
        elems = [page.web_upper_menu.get_btn_menu(),
                 page.web_upper_menu.get_product_sort(),
                 page.web_upper_menu.get_shopping_cart()
                 ]
        Verifications.soft_displayed(elems)

    @staticmethod
    @allure.step('adding product to cart flow')
    def adding_product_to_cart():
        UiActions.click(page.web_products.get_btn_atc_backpack())
        UiActions.click(page.web_products.get_btn_atc_black_shirt())
        UiActions.click(page.web_products.get_btn_atc_onesie())
        UiActions.click(page.web_products.get_btn_atc_bike())
        UiActions.click(page.web_products.get_btn_atc_jacket())
        UiActions.click(page.web_products.get_btn_atc_red_shirt())
        UiActions.click(page.web_upper_menu.get_shopping_cart())

    @staticmethod
    @allure.step('verify number of products flow')
    def verify_number_of_products(number):
        if number > 0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.your_cart_page.products_list)
            Verifications.verify_number_of_elements(page.web_your_cart.get_products_list(), number)

    @staticmethod
    @allure.step('delete products from cart flow')
    def delete_products(by, value):
        if by == 'product':
            UiActions.click(page.web_your_cart.get_delete_by_product_name(value))
        elif by == 'index':
            UiActions.click(page.web_your_cart.get_products_by_index(value))
            UiActions.click(page.web_your_cart.get_delete_product())
            UiActions.click(page.web_your_cart.get_shopping_cart())

    @staticmethod
    @allure.step('go to Swag Lubs login page flow')
    def return_to_swag_lub_login(self):
        self.driver.get(get_data('Url'))

    @staticmethod
    def filling_information(first_name, last_name, postal_code):
        UiActions.click(page.web_upper_menu.get_shopping_cart())
        UiActions.click(page.web_your_cart.get_btn_checkout())
        UiActions.clear(page.web_checkout.get_first_name())
        UiActions.update_text(page.web_checkout.get_first_name(), first_name)
        UiActions.clear(page.web_checkout.get_last_name())
        UiActions.update_text(page.web_checkout.get_last_name(), last_name)
        UiActions.clear(page.web_checkout.get_postal_code())
        UiActions.update_text(page.web_checkout.get_postal_code(), postal_code)

data = read_csv(get_data('CSV_Location'))
testdata = [
    (data[0][0], data[0][1], data[0][2]),
    (data[1][0], data[1][1], data[1][2]),
    (data[2][0], data[2][1], data[2][2])]




