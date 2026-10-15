import os
from config import PATH
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tools import GetLog

class BasePage(object):

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.default_timeout = timeout

    def fd_element(self, loc):
        """
        元素定位的公共方法
        :param loc: 元素属性值
        :return 定位到的元素
        """
        try:
            # 一般写法，元素需可见
            # element = WebDriverWait(self.driver,self.default_timeout).until(EC.visibility_of_element_located(loc))
            # 推荐用下面的写法，元素不可见时也能定位到
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位超时，定位信息：{loc}，错误详情：{e}")
            raise # 重新抛出异常供上层处理

    def base_input(self, loc, text):
        element = self.fd_element(loc)
        element.clear()
        element.send_keys(text)

    def base_click(self, loc):
        ele = self.fd_element(loc)
        ele.click()
        return ele

    def base_assert_text(self,loc,assert_text):
        text = self.fd_element(loc).text
        assert text == assert_text, f"断言错误，预期值 {assert_text} 实际值 {text}"

    def get_shot(self, file_name):
        file_path = os.path.join(PATH, 'img', file_name)
        self.driver.get_screenshot_as_file(file_path)

    def base_switch_handle(self, loc):
        """切换窗口"""
        WebDriverWait(self.driver, self.default_timeout).until(lambda x: len(x.window_handles) > 1)
        handles = self.driver.window_handles
        # -1 表示切换到最新窗口
        self.driver.switch_to.window(handles[-1])

        ele = self.fd_element(loc)
        return ele

    def base_switch_frame(self, loc):
        """切换frame"""
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    def base_default_frame(self):
        """切回默认的frame，也就是上一个frame"""
        self.driver.switch_to.default_content()

    def base_select_list(self, loc, text=None,index=None,value=None):
        """下拉框选择
        :param text : 文本
        :param index : 按下标
        :param value : 按 value 属性
        """
        ele = self.fd_element(loc)
        sel = Select(ele)
        if text is not None:
            sel.select_by_visible_text(text)
        elif index is not None:
            sel.select_by_index(index)
        elif value is not None:
            sel.select_by_value(value)
        else:
            raise ValueError("text, index, value 三选一")