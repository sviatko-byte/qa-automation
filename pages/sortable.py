import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Sortable(BasePage):
    TAB_LIST = (By.ID, 'demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.ID, 'demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.TAB_LIST).click()
        order_before = self.get_sortable_items(self.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.TAB_GRID).click()
        order_before = self.get_sortable_items(self.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.GRID_ITEM)
        return order_before, order_after
