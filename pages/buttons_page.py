from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


class ButtonsPage(MainPage):
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "#rightClickBtn")
    DOUBLE_CLICK_MSG = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_MSG = (By.CSS_SELECTOR, "#rightClickMessage")

    def double_click(self):
        action = ActionChains(self.driver)
        btn = self.wait.until(EC.visibility_of_element_located(self.DOUBLE_CLICK_BTN))
        action.double_click(btn).perform()

    def should_display_double_click_message(self, text):
        self.wait.until(EC.text_to_be_present_in_element(self.DOUBLE_CLICK_MSG, text))

    def right_click(self):
        action = ActionChains(self.driver)
        btn = self.wait.until(EC.visibility_of_element_located(self.RIGHT_CLICK_BTN))
        action.context_click(btn).perform()

    def should_display_right_click_message(self, text):
        self.wait.until(EC.text_to_be_present_in_element(self.RIGHT_CLICK_MSG, text))




