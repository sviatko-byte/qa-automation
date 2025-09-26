import random
import re

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DragabblePage(BasePage):
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0,50), random.randint(0,50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position


    def simple_box(self):
        drag_div = self.element_is_visible(self.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    def get_top_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[2])

    def get_left_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[1])

    def axis_restricted_x(self):
        self.element_is_visible(self.AXIS_TAB).click()
        only_x = self.element_is_visible(self.ONLY_X)
        position = self.get_before_and_after_position(only_x)
        top_x_before = self.get_top_position(position[0])
        top_x_after = self.get_top_position(position[1])
        left_x_before = self.get_left_position(position[0])
        left_x_after = self.get_left_position(position[1])
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    def axis_restricted_y(self):
        self.element_is_visible(self.AXIS_TAB).click()
        only_y = self.element_is_visible(self.ONLY_Y)
        position_x = self.get_before_and_after_position(only_y)

        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])

        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])

        return [top_x_before, top_x_after], [left_x_before, left_x_after]

