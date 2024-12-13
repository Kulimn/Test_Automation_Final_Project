import test_cases.conftest as conf
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.checkout_complete_page import CheckoutCompletePage
from page_objects.web_objects.checkout_overview_page import CheckoutOverviewPage
from page_objects.web_objects.checkout_page import CheckoutPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.products_page import ProductsPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from page_objects.web_objects.your_cart_page import YourCartPage

# Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_products = None
web_your_cart = None
web_checkout = None
web_checkout_overview = None
web_checkout_complete = None

# Mobile Objects
mobile_calculator = None
mobile_saved = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_products'] = ProductsPage(conf.driver)
        globals()['web_your_cart'] = YourCartPage(conf.driver)
        globals()['web_checkout'] = CheckoutPage(conf.driver)
        globals()['web_checkout_overview'] = CheckoutOverviewPage(conf.driver)
        globals()['web_checkout_complete'] = CheckoutCompletePage(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)
