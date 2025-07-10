from wsgiref.util import request_uri
from selenium.webdriver.common.by import By
import requests

from pages.base_page import BasePage


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, '#simpleLink')
    BAD_REQUEST = (By.CSS_SELECTOR, '#bad-request')


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        response = requests.get(link_href)

        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return url
        else:
            return response.status_code

    def check_broken_link(self):
        simple_link = self.element_is_visible(self.locators.BAD_REQUEST)
        simple_link.value_of_css_property('Bad Request')


