from selenium.webdriver.common.by import By

first_name = (By.ID, 'first-name')
last_name = (By.ID, 'last-name')
postal_code = (By.ID, 'postal-code')
btn_cancel = (By.ID, 'cancel')
btn_continue = (By.ID, 'continue')


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_name(self):
        return self.driver.find_element(first_name[0], first_name[1])

    def get_last_name(self):
        return self.driver.find_element(last_name[0], last_name[1])

    def get_postal_code(self):
        return self.driver.find_element(postal_code[0], postal_code[1])

    def get_btn_cancel(self):
        return self.driver.find_element(btn_cancel[0], btn_cancel[1])

    def get_btn_continue(self):
        return self.driver.find_element(btn_continue[0], btn_continue[1])
