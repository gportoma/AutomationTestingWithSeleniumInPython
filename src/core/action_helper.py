from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class ActionHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Ajuste o tempo de espera conforme necessário

    def type(self, locator, text):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Element with locator {locator} not clickable.")

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            print(f"Element with locator {locator} not clickable.")

    def select_by_visible_text(self, locator, text):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            Select(element).select_by_visible_text(text)
        except TimeoutException:
            print(f"Element with locator {locator} not found.")
