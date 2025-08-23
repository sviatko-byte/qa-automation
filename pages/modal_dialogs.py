
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
        SMALL_MODAL_BUTTON = 'showSmallModal'
        SMALL_MODAL_BUTTON_CLOSE = 'closeSmallModal'
        TITLE_SMALL_MODAL = 'example-modal-sizes-title-sm'
        BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')


        LARGE_MODAL_BUTTON = 'showLargeModal'
        LARGE_MODAL_BUTTON_CLOSE = 'closeLargeModal'
        TITLE_LARGE_MODAL = 'example-modal-sizes-title-lg'
        BODY_LARGE_MODAL = 'example-modal-sizes-title-lg'


        def small_modal_modal_clic(self):
            self.element_is_present(self.SMALL_MODAL_BUTTON).click()
            title_smal = self.element_is_visible(self.TITLE_SMALL_MODAL).text
            body_small_text = self.element_is_visible(self.BODY_SMALL_MODAL).text
            self.element_is_present(self.SMALL_MODAL_BUTTON_CLOSE).click()
            self.element_is_present(self.LARGE_MODAL_BUTTON).click()
            title_large = self.element_is_visible(self.TITLE_LARGE_MODAL).text
            body_large_text = self.element_is_visible(self.BODY_SMALL_MODAL).text

