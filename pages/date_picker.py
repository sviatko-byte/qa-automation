from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from faker import Faker

class DatePicker(BasePage):
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')

    fake_en = Faker("en_US")

    def select_date(self):
        # 1. генеруємо випадкову дату
        random_date = self.fake_en.date_of_birth(minimum_age=18, maximum_age=60)

        # 2. клікаємо по інпуту, щоб відкрився календар
        self.element_is_clickable(self.DATE_INPUT).click()

        # 3. вибираємо місяць
        month_dropdown = Select(self.element_is_visible(self.DATE_SELECT_MONTH))
        month_dropdown.select_by_index(random_date.month - 1)  # індексація з 0

        # 4. вибираємо рік
        year_dropdown = Select(self.element_is_visible(self.DATE_SELECT_YEAR))
        year_dropdown.select_by_value(str(random_date.year))

        # 5. вибираємо день
        days = self.elements_are_visible(self.DATE_SELECT_DAY_LIST)
        for day in days:
            if day.text == str(random_date.day) and "outside-month" not in day.get_attribute("class"):
                day.click()
                break

        return random_date
