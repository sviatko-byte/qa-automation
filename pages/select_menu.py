import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from helpers import get_random_color_name


class SelectMenu(BasePage):
    SELECT_OPTION = (By.ID, 'withOptGroup')
    SELECT_OPTION_INPUT = "//div[contains(@class,'option') and text()='{text}']"

    SELECT_TITLE = (By.ID, 'selectOne')
    SELECT_TITLE_INPUT = "//div[contains(@class,'option') and text()='{text}']"

    SELECT_MENU = (By.ID, 'oldSelectMenu')

    def select_option_by_text(self, text: str):
        dropdown = self.element_is_present(self.SELECT_OPTION)
        dropdown.click()
        option = self.element_is_visible((By.XPATH, self.SELECT_OPTION_INPUT.format(text=text)))
        option.click()

    def select_title_by_text(self, text: str = "Dr."):
        dropdown = self.element_is_present(self.SELECT_TITLE)
        dropdown.click()
        option = self.element_is_visible((By.XPATH, self.SELECT_TITLE_INPUT.format(text=text)))
        option.click()

    def select_random_color(self):
        element = self.element_is_present(self.SELECT_MENU)
        select = Select(element)
        color = get_random_color_name()
        select.select_by_visible_text(color)
        return color
