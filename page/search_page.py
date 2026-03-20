from base.base_page import BasePage
from selenium.webdriver.common.by import By
class SearchPage(BasePage):
    def __init__(self):
        super().__init__()

    def JP_Enter_JPet_Desc_By_ID(self,product_id):
        self.find_el((By.XPATH,"//a[text()="+product_id+"]")).click()

    def JP_Enter_Sub_JPet_Desc_By_ItemID(self,item_id):
        self.find_el((By.XPATH,"//a[text()="+item_id+"]")).click()

