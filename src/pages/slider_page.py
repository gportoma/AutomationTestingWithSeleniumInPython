from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.slider_handle = "#slider a.ui-slider-handle"

    def select_50_percent_in_slider(self):
        slider_handle_element = self.driver.find_element(By.CSS_SELECTOR, self.slider_handle)
        script = "arguments[0].style.left = '50%';"
        self.driver.execute_script(script, slider_handle_element)

