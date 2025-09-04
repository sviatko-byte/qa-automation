
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')



    def check_menu(self):
        menu_item_list = self.element_are_present(self.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
          self.action_move_to_element(item)
          data.append(item.text)
        return data

