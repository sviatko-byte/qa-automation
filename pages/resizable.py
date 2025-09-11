import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResizablePage(BasePage):
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'id="resizable"')

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size
        height = value_of_size
        return width,  height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE),200, 100)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE), random.randint(1, 200), random.randint(1, 200))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE), random.randint(1, 200), random.randint(1, 200))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        return max_size, min_size


