
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
        SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
        SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
        BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
        TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

        LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
        BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
        TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')

        def small_modal_modal(self):
            self.element_is_visible(self.SMALL_MODAL_BUTTON).click()
            title_small = self.element_is_visible(self.TITLE_SMALL_MODAL).text
            body_small_text = self.element_is_visible(self.BODY_SMALL_MODAL).text
            self.element_is_visible(self.SMALL_MODAL_CLOSE_BUTTON).click()

            self.element_is_visible(self.LARGE_MODAL_BUTTON).click()
            title_large = self.element_is_visible(self.TITLE_LARGE_MODAL).text
            body_large_text = self.element_is_visible(self.BODY_LARGE_MODAL).text

            return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
