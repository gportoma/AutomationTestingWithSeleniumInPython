from selenium.webdriver.common.by import By
from src.core.action_helper import ActionHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DatePickerPage:
    def __init__(self, driver):
        self.driver = driver
        self.action_helper = ActionHelper(driver)
        self.date_picker_disabled = (By.ID, "datepicker1")
        self.date_picker_enabled = (By.ID, "datepicker2")
        self.close_date_picker = (By.XPATH, "//a[@title='Close the datepicker']")

    def type_date_picker_enabled(self, date_picker):
        self.action_helper.type(self.date_picker_enabled, date_picker)
        self.action_helper.click(self.close_date_picker)

    def select_birth_date(self, desired_date):
        self.action_helper.click(self.date_picker_disabled)

        date_parts = desired_date.split("/")
        desired_day = int(date_parts[0])
        desired_month = int(date_parts[1])
        desired_year = int(date_parts[2])

        while True:
            month_year_element = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-title")
            month_year_text = month_year_element.text
            month_year_parts = month_year_text.split(" ")
            current_month = month_year_parts[0]
            current_year = int(month_year_parts[1])

            if current_month == self.get_month_name(desired_month) and current_year == desired_year:
                break
            prev_button = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-prev")
            self.action_helper.click(prev_button)

        day_element = self.driver.find_element(By.XPATH, f"//a[text()='{desired_day}']")
        self.action_helper.click(day_element)

    @staticmethod
    def get_month_name(month):
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return month_names[month - 1]
        