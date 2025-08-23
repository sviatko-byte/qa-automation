from selenium.webdriver.common.by import By




class NestedFramesPage:
    def __init__(self, driver):
        self.driver = driver

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

    def check_nested_frames_page(self):
        parent_frame = self.driver.find_element(*self.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.driver.find_element(*self.PARENT_TEXT).text
        child_frame = self.driver.find_element(*self.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.driver.find_element(*self.CHILD_TEXT).text
        self.driver.switch_to.default_content()

        return parent_text, child_text