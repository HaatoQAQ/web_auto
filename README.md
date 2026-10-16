# web自动化测试项目

## 技术栈
- Python
- Selenium
- Pytest
- Allure
- JSON

## 项目结构
- config：配置
- base：基础方法
- data：测试数据
- page：页面封装
- script：测试用例

## 运行方式
pip install -r requirements.txt
pytest

## 生成 Allure 报告
pytest --alluredir=./results
## 网页查看
allure serve ./results
## 生成离线报告
allure generate ./results -o ./allure-report --clean
## 打开测试报告
allure open ./allure-report

## 覆盖场景
- 登录，查看商品信息，添加，删除购物车，填写信息，下单支付
- 参数化
- 异常场景
- 断言封装
- 数据驱动