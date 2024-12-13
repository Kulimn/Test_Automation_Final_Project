import allure
import pytest

from utilities.common_ops import get_data, By, Product_Type
from workflow import web_flows
from workflow.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
    @allure.title('Test01: Verify Login Swag Labs')
    @allure.description('This test verifies a successful login Swag Labs')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('UserName'), (get_data('Password')))
        WebFlows.verify_swag_labs_title('Swag Labs')

    @allure.title('Test02: Verify Upper Menu Buttons')
    @allure.description('This test verifies upper menu buttons displayed')
    def test_verify_upper_menu(self):
        WebFlows.login_flow(get_data('UserName'), (get_data('Password')))
        WebFlows.verify_menu_buttons_flow_smart_assertions()  # smart-assertion
        # WebFlows.verify_menu_buttons_flow_my_implementation() # my implementation

    @allure.title('Test03: Verify Adding And Removing Products From Cart ')
    @allure.description('This test verifies adding and deleting products to cart')
    def test_verify_addind_products(self):
        WebFlows.login_flow(get_data('UserName'), (get_data('Password')))
        WebFlows.adding_product_to_cart()
        WebFlows.delete_products(By.PRODUCT, Product_Type.BACKPACK) # Delete Product By Name
        WebFlows.delete_products(By.INDEX, 4)                 # Delete Product By Index
        WebFlows.verify_number_of_products(4)

    @allure.title('Test04: Verify Customers Information Entry During Checkout ')
    @allure.description('This test verifies inserting customers information')
    @pytest.mark.parametrize('first_name,last_name,postal_code', web_flows.testdata)
    def test_checkout_information(self, first_name, last_name, postal_code):
        WebFlows.login_flow(get_data('UserName'), (get_data('Password')))
        WebFlows.filling_information(first_name, last_name, postal_code)


    def teardown_method(self):
        WebFlows.return_to_swag_lub_login(self)

