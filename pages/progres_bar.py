import random
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProgressBar(BasePage):

    PROGRESS_BAR_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR_VALUE = (By.ID, "progressBar")

    def progress_bar_click(self):
        value_before = self.element_is_visible(self.PROGRESS_BAR_VALUE).text
        progress_bar_button =self.element_is_visible(self.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2,10))
        progress_bar_button.click()
        value_after = self.element_is_visible(self.PROGRESS_BAR_VALUE).text
        return value_after, value_before
