from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Tooltips(BasePage):

        HOVER_BUTTON = (By.ID, "toolTipButton")
        TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

        FAILED_INPUT = (By.ID, "toolTipTextField")
        TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

        CONTRARY_LINK = (By.CSS_SELECTOR, "div[class='col-12 mt-4 col-md-6'] a:nth-child(1)")
        TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

        SECTION_LINK = (By.CSS_SELECTOR, "a:nth-child(2)")
        TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

        TOOL_TIPS_INNERS = (By.CSS_SELECTOR, "#texToolTopContainer")

        def get_text_from_tool_tips(self, hover_elem, wait_elem):
            element = self.element_is_present(hover_elem)
            self.action_move_to_element(element)
            self.element_is_visible(wait_elem)
            tool_tip_text = self.element_is_visible(self.TOOL_TIPS_INNERS)
            text = tool_tip_text.text
            return text

        def check_tool_tips(self):
            tool_tips_text_button = self.get_text_from_tool_tips(self.HOVER_BUTTON, self.TOOL_TIP_BUTTON)
            tool_tips_text_filed = self.get_text_from_tool_tips(self.FAILED_INPUT, self.TOOL_TIP_FIELD)
            tool_tips_text_contrary = self.get_text_from_tool_tips(self.CONTRARY_LINK, self.TOOL_TIP_CONTRARY)
            tool_tips_text_section = self.get_text_from_tool_tips(self.SECTION_LINK, self.TOOL_TIP_SECTION)
            return tool_tips_text_button, tool_tips_text_filed, tool_tips_text_contrary, tool_tips_text_section




