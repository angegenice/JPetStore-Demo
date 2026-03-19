from utils import DriverUtils
from page.index_page import IndexPage
from page.login_page import LoginPage
import time
class TestIndex():
    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    def setup_method(self):
        self.driver.get("https://jpetstore.aspectran.com/")

    def teardown_class(self):
        DriverUtils.quit_driver()

    def teardown_method(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
    
    # def test_index(self):
    #     """测试首页"""
    #     index  = IndexPage()
    #     # 首页
    #     index.JP_Enter_SignIn()
    #     time.sleep(2)
    
    def test_login(self):
        """登录测试"""
        index  = IndexPage()
        # 首页
        index.JP_Enter_SignIn()
        time.sleep(2)
        # 登录
        login = LoginPage()
        login.JP_login("admin","123456")
        time.sleep(2)


