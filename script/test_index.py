from utils import DriverUtils
from page.index_page import IndexPage
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
    
    def test_index(self):
        index  = IndexPage()
        # 首页
        index.JP_Enter_SignIn()
        time.sleep(2)

