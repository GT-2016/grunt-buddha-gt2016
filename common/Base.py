# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains        # 模拟鼠标
from selenium.webdriver.support.select import Select            # 下拉框

class Base(object):
    "Base class for common functions"

    def __init__(self, driver):
        "初始化"
        # if browser == 'firefox' or browser == 'f':
        #     profile_firefox = 'C://Users//Administrator//AppData//Roaming//Mozilla//Firefox//Profiles//ardla6e5.default'
        #     profile = webdriver.FirefoxProfile(profile_firefox)
        #     self.driver = webdriver.Firefox(profile)
        # elif browser == 'Chrome' or browser == 'c':
        #     options = webdriver.ChromeOptions()
        #     options.add_argument('--user-data-dir=C://Users//Administrator//AppData//Local//Google//Chrome//User Data')
        #     self.driver = webdriver.Chrome(chrome_options = options)
        # elif browser == 'Ie' or browser == 'i':
        #     self.driver = webdriver.Ie()
        # elif browser == 'Edge' or browser == 'e':
        #     self.driver = webdriver.Edge()
        # elif browser == 'Safari' or browser == 's':
        #     self.driver = webdriver.Safari()
        # else:
        #     raise NameError('Only input firefox Chrome Ie Edge Safari')

        self.driver = driver
        self.timeout = 10
        self.poll = 0.5
        # self.driver.implicitly_wait(2)

    def set_size(self, a, b):
        "设置窗口大小"
        self.driver.set_window_size(a, b)

    def set_max_size(self):
        "窗口最大化"
        self.driver.maximize_window()

    def set_back(self):
        "窗口后退"
        self.driver.back()

    def set_forward(self):
        "窗口前进"
        self.driver.forward()

    def get_url(self,url):
        "get url"
        self.driver.get(url)

    def get_title(self):
        "获取title"
        print('current page is %s'%self.driver.title)

    def get_cur_url(self):
        "获取url地址"
        print("current page url is %s"%self.driver.current_url)
    def get_attr(self,ele, type):
        "获取属性"
        return ele.get_attribute(type)
    def get_css_attr(self, ele, type):
        "获取css属性"
        return ele.value_of_css_property(type)
    def _get_cookie(self):
        return self.driver.get_cookies()

    def find_ele(self, args):
        """
        :param args: 传元祖 (by,value)
        by_id= "id"
        by_xpath = "xpath"
        by_link_text = "link text"
        by_partial_text = "partial link text"
        by_name = "name"
        by_tag_name = "tag name"
        by_class_name = "class name"
        by_css_selector = "css selector"
        :return:  元素
        """
        ele = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x:x.find_element(*args))
        return ele
    def find_eles(self, args):
        "查找某些元素"
        eles = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x:x.find_elements(*args))
        return eles
    def _click(self, args):
        "点击元素"
        ele = self.find_ele(args)
        ele.click()
    def _send(self, args, text):
        "模拟键盘输入"
        ele = self.find_ele(args)
        ele.send_keys(text)
    def _sendKey(self, args, locator):
        """
        发送组合键
        :param args: 元素定位
        :locator args:(Keys.CONTROL,'a')
        :return:
        """
        ele = self.find_ele(args)
        ele.send_keys(locator)

    def _clear(self, args):
        "清空内容"
        ele = self.find_ele(args)
        ele.clear()

    def move_to_select(self,ele, locator):
        "鼠标移动到link上，然后定位点击某个下拉选项"
        webdriver.ActionChains(self.driver).move_to_element(ele).perform()      # 自带
        # time.sleep(1)
        self._click(locator)
    def move_to(self, ele):
        """
        使用ActionChains模拟
        * key_down。模拟按键按下
        * key_up。模拟按键弹起
        * click
        * send_keys
        * double_click。鼠标左键双击
        * click_and_hold。鼠标左键点击住不放
        * release。鼠标左键弹起，可以与click_and_hold配合使用
        * move_to_element。把鼠标移动到元素的中心点
        * context_click。鼠标右键点击
        * drag_and_drop。拖拽
        """
        ActionChains(self.driver).move_to_element(ele)


    def is_visibility(self, args):
        "元素是否可见，传定位"
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.visibility_of_element_located(args))
            return eles
        except:
            return False
    def is_visible(self,ele):
        "元素是否可见，传元素"
        try:
            flag = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.visibility_of(ele) ,"visibility_of failed")
            return flag
        except:
            return False
    def is_alert(self):
        "是否存在alert框"
        try:
            flag = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.alert_is_present)
            return flag
        except:
            return False

    def _isSelected(self, ele):
        "元素是否被选中，radio或checkbox，封装意义不大"
        return ele.is_selected()

    def _isEnable(self, ele):
        "元素是否灰化,封装意义不大"
        return ele.is_enabled()

    def executeJS(self, script, ele):
        """
        执行JS脚本:script
        ele：在定位的元素上执行
        """
        # 例如隐藏元素 ("$(arguments[0]).fadeOut()",ele)
        self.driver.execute_script(script, ele)
    def _alert(self):
        """
        alert操作：alert/confirm/prompt
        :text 返回alert/confirm/prompt中的文字信息
        :accept 确认
        :dismiss 取消，如果有
        :send_keys prompt输入文字
        :return:
        """
        alert = self.driver.switch_to_alert()
        return alert

    def _select(self, sel):
        "select选项操作"
        """
        * options: 返回下拉框里所有的选项
        * all_selected_options: 返回所有选中的选项
        * select_by_value(value): 通过option的value值来选择
        * select_by_index(index) 通过option的顺序来选择
        * select_by_visible_text(text): 通过option的text来选择
        """
        pass

    def deleteCookie(self):
        "删除cookies"
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_logout(self):
        "登录后保存cookies，然后删除，再根据cookies登录"
        "以百度为例"
        cookie = base._get_cookie()
        base.deleteCookie()
        time.sleep(4)
        print('delete')
        driver.add_cookie({'name': 'BAIDUID', 'value': cookie[0]['value']})
        driver.add_cookie({'name': 'BDUSS', 'value': cookie[4]['value']})
        url = "https://www.baidu.com"
        driver.get(url)


    def close(self):
        "关闭并退出"
        time.sleep(5)
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    # options = webdriver.ChromeOptions()
    # options.add_argument('--user-data-dir=C://Users//Administrator//AppData//Local//Google//Chrome//User Data')
    # driver = webdriver.Chrome(chrome_options = options)
    # profile_firefox = 'C://Users//Administrator//AppData//Roaming//Mozilla//Firefox//Profiles//ardla6e5.default'
    # profile = webdriver.FirefoxProfile(profile_firefox)
    # driver = webdriver.Firefox(profile)
    driver = webdriver.Chrome()
    url = "https://dict.hjenglish.com/"
    url = "https://www.baidu.com"
    driver.get(url)
    base = Base(driver)
    ele = base.find_ele(("link text","设置"))
    print(ele)
    base.close()
