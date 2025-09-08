from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.helpers import get_random_color_name


class SelectMenu(BasePage):
    SELECT_OPTION = (By.ID, 'withOptGroup')
    SELECT_OPTION_INPUT = "//div[contains(@class,'option') and text()='{text}']"

    SELECT_TITLE = (By.ID, 'selectOne')
    SELECT_TITLE_INPUT = "//div[contains(@class,'option') and text()='{text}']"

    SELECT_MENU = (By.ID, 'oldSelectMenu')
    MULTISELECT = (By.ID, 'react-select-4-input')
    CARS = (By.ID, 'cars')

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
        print(f"DEBUG: вибраний колір з хелпера -> {color}")
        if not color:
            raise ValueError("Хелпер повернув None!")
        select.select_by_visible_text(color)
        return color

    def multiselect_drop_by_text(self, text: str = "Red"):
        input_field = self.element_is_present(self.MULTISELECT)
        input_field.send_keys(text)
        input_field.send_keys(Keys.ENTER)

    def select_car_by_name(self, car_name: str = "Volvo"):
        element = self.element_is_present(self.CARS)
        select = Select(element)
        select.select_by_visible_text(car_name)
        return car_name
