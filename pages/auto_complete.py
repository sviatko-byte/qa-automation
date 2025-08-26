from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import get_random_color_name


class Auto(BasePage):

    MULTIPLE_INPUT = (By.ID, "autoCompleteMultipleInput")
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class= "css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div.css-1rhbuit-multiValue svg')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '.auto-complete__indicators')

    def fill_input_multi(self):
        color = get_random_color_name()
        input_multi = self.element_is_clickable(self.MULTIPLE_INPUT)
        input_multi.send_keys(color)
        input_multi.send_keys(Keys.ENTER)

    def remove_value_from_multi(self):
        values = self.elements_are_visible(self.MULTI_VALUE)
        count_before = len(values)

        remove_buttons = self.elements_are_visible(self.MULTI_VALUE_REMOVE)
        if remove_buttons:
            remove_buttons[0].click()  # видаляємо перший елемент

        values_after = self.elements_are_visible(self.MULTI_VALUE)
        count_after = len(values_after)

        return count_after, count_before