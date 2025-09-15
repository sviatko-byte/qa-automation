import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Droppable(BasePage):
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # --- Accept ---
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # --- Prevent Propagation ---
    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # --- Revert Draggable ---
    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


    def drope_simple(self):
        self.element_is_visible(self.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div

    def drope_accept(self):
        self.element_is_visible(self.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        return drop_div, not_acceptable_div , acceptable_div

    def drop_prevent_propogation(self):
        self.element_is_visible(self.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        return drag_div, not_greedy_inner_box, greedy_inner_box

    def drop_will_revert(self):
        revert_tab = self.element_is_visible(self.REVERT_TAB, timeout=10)
        revert_tab.click()
        self.wait_for_element_attribute(self.REVERT_TAB, "class", "active", timeout=10)
        will_revert = self.element_is_visible(self.WILL_REVERT, timeout=10)
        drop_zone = self.element_is_visible(self.DROP_HERE_REVERT, timeout=10)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", will_revert)
        self.action_drag_and_drop_to_element(will_revert, drop_zone)
        style_after_move = will_revert.get_attribute('style')
        time.sleep(2)
        style_after_revert = will_revert.get_attribute('style')
        return style_after_move, style_after_revert