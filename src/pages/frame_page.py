from selenium.webdriver.common.by import By
from src.core.action_helper import ActionHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FramePage:
    def __init__(self, driver):
        self.driver = driver
        self.action_helper = ActionHelper(driver)
        self.single_iframe = (By.XPATH, "//iframe[@id='singleframe']")
        self.input_single_frame = (By.XPATH, "//input[@type='text']")

    def type_in_single_frame(self, msg):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "singleframe")))
        self.action_helper.type(self.input_single_frame,msg)