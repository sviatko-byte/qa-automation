from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Frames(BasePage):
    FIRST_FRAME = (By.ID, 'frame1')
    SECOND_FRAME = (By.ID, 'frame2')
    TITLE_FRAME = (By.ID, 'sampleHeading')

    def check_frames(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.element_is_present(self.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME).text
            return [text, width, height]
