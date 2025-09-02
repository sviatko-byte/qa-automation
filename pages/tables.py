from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TablesPage(BasePage):

    TABS_WHAT = ( By.ID,'demo-tab-what')
    TABS_WHAT_CONTENT = ( By.ID,'demo-tabpane-what')
    TABS_ORIGIN = ( By.ID,'demo-tab-origin')
    TABS_ORIGIN_CONTENT = ( By.ID,'demo-tabpane-origin')
    TABS_USER = ( By.ID,'demo-tab-use')
    TABS_USER_CONTENT = ( By.ID,'demo-tabpane-use')



    def check_tabs(self):
        what_button = self.element_is_visible(self.TABS_WHAT)
        origin_button = self.element_is_visible(self.TABS_ORIGIN)
        use_button = self.element_is_visible(self.TABS_USER)
        what_button.click()
        what_content = self.element_is_visible(self.TABS_WHAT_CONTENT).text
        origin_button.click()
        origin_content = self.element_is_visible(self.TABS_ORIGIN_CONTENT).text
        use_button.click()
        user_content = self.element_is_visible(self.TABS_USER_CONTENT).text
        print(what_content, origin_content, user_content, )
