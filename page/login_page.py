from base.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.login_btn = (By.XPATH,"//button[@type='submit']")

    def JP_login(self,username,password):
        """登录"""
        self.input_text(self.find_el(self.username),username)
        self.input_text(self.find_el(self.password),password)
        self.find_el(self.login_btn).click()
