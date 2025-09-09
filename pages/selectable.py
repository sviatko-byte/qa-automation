import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SelectablePage(BasePage):
        TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
        LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
        LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

        TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
        GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
        GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')

        def get_sortable_items(self, elements):
            item_list = self.elements_are_visible(elements)
            return [item.text for item in item_list]

        def change_list_order(self):
            self.element_is_visible(self.TAB_LIST).click()
            order_before = self.get_sortable_items(self.LIST_ITEM)
            item_list = random.sample(self.elements_are_visible(self.LIST_ITEM), k=2)
            self.action_drag_and_drop_to_element(item_list[0], item_list[1])
            order_after = self.get_sortable_items(self.LIST_ITEM)
            return order_before, order_after

        def change_grid_order(self):
            self.element_is_visible(self.TAB_GRID).click()
            order_before = self.get_sortable_items(self.GRID_ITEM)
            item_list = random.sample(self.elements_are_visible(self.GRID_ITEM), k=2)
            self.action_drag_and_drop_to_element(item_list[0], item_list[1])
            order_after = self.get_sortable_items(self.GRID_ITEM)
            return order_before, order_after


