from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class OrderPage(BasePage):
    def __init__(self):
        super().__init__()
        self.add_cart = (By.XPATH,"//a[text()='Add to Cart']")
        self.check_out = (By.XPATH,"//a[text()='Proceed to Checkout']")
        """order_text"""
        # 卡分类菜单
        self.card_type_select = (By.NAME,"cardType")
        self.card_number = (By.NAME,"creditCard")
        self.expiry_date = (By.NAME,"expiryDate")
        self.first_name = (By.NAME,"billToFirstName")
        self.last_name = (By.NAME,"billToLastName")
        # billAddress2
        self.address1 = (By.NAME,"billAddress1")
        self.address2 = (By.NAME,"billAddress2")
        # billCity
        self.bill_city = (By.NAME,"billCity")
        self.bill_state = (By.NAME,"billState")
        self.bill_zip = (By.NAME,"billZip")
        self.bill_country = (By.NAME,"billCountry")
        self.checkbox = (By.NAME,"shippingAddressRequired")
        self.continue_btn = (By.XPATH,"//button[text()='Continue']")
    
    def JP_Add_Cart(self):
        self.find_el(self.add_cart).click()

    def JP_Check_Out(self):
        self.find_el(self.check_out).click()

    def JP_Comfirm_Order(self,card_type:int,card_number,expiry_date,first_name,last_name,address1,address2,bill_city,
                         bill_state,bill_zip,bill_country):
        Select(self.find_el(self.card_type_select)).select_by_index(card_type)
        self.input_text(self.find_el(self.card_number),card_number)
        self.input_text(self.find_el(self.expiry_date),expiry_date)
        self.input_text(self.find_el(self.first_name),first_name)
        self.input_text(self.find_el(self.last_name),last_name)
        self.input_text(self.find_el(self.address1),address1)
        self.input_text(self.find_el(self.address2),address2)
        self.input_text(self.find_el(self.bill_city),bill_city)
        self.input_text(self.find_el(self.bill_state),bill_state)
        self.input_text(self.find_el(self.bill_zip),bill_zip)
        self.input_text(self.find_el(self.bill_country),bill_country)
        self.find_el(self.check_out).click()
        # if checkbox.is_selected():
        #     print("Checkbox 已选中")
        # else:
        #     print("Checkbox 未选中")
        self.find_el(self.continue_btn).click()







    