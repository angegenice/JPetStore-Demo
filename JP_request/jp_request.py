import requests
from requests import Session

session = Session()
url = "https://jpetstore.aspectran.com/account/signonForm"
header = {
    "Content-Type" : "application/x-www-form-urlencoded"
}
form_data = {
    "username":"hhh",
    "password":"123456"
}
# json格式数据用json=data
res = session.post(url=url,headers=header,data=form_data)
print(res)
session.close()