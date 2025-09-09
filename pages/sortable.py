from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Sortable (BasePage):
    TAB_LIST = (By.ID, 'demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.ID, 'demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')




