import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Droppable(BasePage):
    # --- Simple ---
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

    # --- Helper: drag & drop ---
    def action_drag_and_drop_to_element(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    # --- Simple Tab ---
    def drope_simple(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SIMPLE_TAB))
        tab.click()
        WebDriverWait(self.driver, 10).until(
            lambda x: "active" in x.find_element(*self.SIMPLE_TAB).get_attribute("class")
        )

        drag_div = self.element_is_visible(self.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.DROP_HERE_SIMPLE)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", drag_div)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div

    # --- Accept Tab ---
    def drope_accept(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_TAB))
        tab.click()
        WebDriverWait(self.driver, 10).until(
            lambda x: "active" in x.find_element(*self.ACCEPT_TAB).get_attribute("class")
        )

        acceptable_div = self.element_is_visible(self.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.DROP_HERE_ACCEPT)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", acceptable_div)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)

        return drop_div, not_acceptable_div, acceptable_div

    # --- Prevent Propagation Tab ---
    def drop_prevent_propogation(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PREVENT_TAB))
        tab.click()
        WebDriverWait(self.driver, 10).until(
            lambda x: "active" in x.find_element(*self.PREVENT_TAB).get_attribute("class")
        )

        drag_div = self.element_is_visible(self.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.GREEDY_INNER_BOX)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", drag_div)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)

        return drag_div, not_greedy_inner_box, greedy_inner_box

    # --- Revert Draggable Tab ---
    def drop_will_revert(self):
        tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.REVERT_TAB))
        tab.click()
        WebDriverWait(self.driver, 10).until(
            lambda x: "active" in x.find_element(*self.REVERT_TAB).get_attribute("class")
        )

        will_revert = self.element_is_visible(self.WILL_REVERT)
        drop_zone = self.element_is_visible(self.DROP_HERE_REVERT)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", will_revert)
        time.sleep(0.5)
        self.action_drag_and_drop_to_element(will_revert, drop_zone)

        style_after_move = will_revert.get_attribute('style')
        time.sleep(2)
        style_after_revert = will_revert.get_attribute('style')

        return style_after_move, style_after_revert
