# 项目配置相关文件
import os
from faker import Faker
# 获取项目路径
PATH = os.path.dirname(__file__)

BASE_URL = "https://www.saucedemo.com/"
BACK_URL = "http://121.43.169.97:8082"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# 人的信息
fk = Faker(locale="zh_CN")

NAME = fk.name()
PHONE = fk.phone_number()
CARD = fk.ssn()