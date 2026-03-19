from base.base_page import BasePage
from utils import DriverUtils
from selenium.webdriver.common.by import By
import time
class IndexPage(BasePage):

    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.signIn_btn = (By.XPATH,"//a[text()='Sign In']")
        self.SignUp_btn = (By.XPATH,"//a[text()='Sign Up']")
        self.search_text = (By.XPATH,"//input[@type='search']")
        self.search_btn = (By.XPATH,"//button[@type='button']")

    def JP_Enter_SignIn(self):
        """进入登录界面"""
        self.find_el(self.signIn_btn).click()



if __name__ == "__main__":

    index  = IndexPage()
    # 首页
    index.driver.get("https://jpetstore.aspectran.com/")
    index.JP_Enter_SignIn()
    time.sleep(2)
    index.driver.quit()
    
