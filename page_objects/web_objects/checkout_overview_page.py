from selenium.webdriver.common.by import By

btn_finish = (By.ID, 'finish')


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_finish(self):
        return self.driver.find_elements(btn_finish[0], btn_finish[1])
