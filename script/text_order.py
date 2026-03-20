from utils import DriverUtils
from page.index_page import IndexPage
from page.login_page import LoginPage
import time
class TestOrder():
    def setup_class(self):
        self.driver = DriverUtils.get_driver()

    def setup_method(self):
        # self.driver.get("https://jpetstore.aspectran.com/account/signonForm")
        # https://jpetstore.aspectran.com/
        self.driver.get("https://jpetstore.aspectran.com/")

    def teardown_class(self):
        DriverUtils.quit_driver()

    def teardown_method(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")
        # pass

    def test_search_order(self):
        """搜索下单"""
        index  = IndexPage()
        # # 登录
        # login = LoginPage()
        # login.JP_login("admin","123456")
        # # 搜索
        index.JP_Search("Angelfish")