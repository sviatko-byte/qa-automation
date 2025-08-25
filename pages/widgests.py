from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Widgets(BasePage):

    SECTION_FIRST = (By.ID, "section1Heading")
    SECTION_CONTENT_FIRST = (By.ID, "section1Content")
    SECTION_SECOND = (By.ID,"section2Heading")
    SECTION_CONTENT_SECOND = (By.ID,"section2Content")
    SECTION_THIRD = (By.ID,"section3Heading")
    SECTION_CONTENT_THIRD = (By.ID,"section3Content")

    def check_accordian(self, accordian_num):
        acordian = {'first':
                        { 'title': self.SECTION_FIRST,
                          'content': self.SECTION_CONTENT_FIRST},
                    'second':
                        { 'title': self.SECTION_SECOND,
                          'content': self.SECTION_CONTENT_SECOND},
                    'third':
                        { 'title': self.SECTION_THIRD,
                          'content': self.SECTION_CONTENT_THIRD},
                        }
        section_title = self.element_is_present(acordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_present(acordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_present(acordian[accordian_num]['content']).text
        print(section_title.text)
        print(section_content)
