
from  selenium  import webdriver
import time
from enum import Enum
from util import urlutil
# 导入三个包
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

# from selenium.webdriver.support.wait import WebDriverWait

class  StartFirfox(object):

    # 定义类被实例化的时候才会被执行的方法，初始化

    # 打开浏览器
    def OpenFirefox(self,url):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)
        #设置等待时间
        # self.WebwaitSleep(self.driver.title)
        # self.ImplicitySleep(2)


    # 关闭浏览器
    def CloseFirfox(self):
        self.driver.quit()

    def GetTitle(self):
        return self.driver.title

    def SwitchFrame(self,id):
        self.driver.switch_to_frame(self.Findid(id))

    def ClickLinkText(self,linktext):
        self.FindLinktext(linktext).click()
        time.sleep(2)

    def Clear(self,widget):
        self.Findid(widget).clear()

    # 浮动的封装
    def ActionMove(self,cls):
        classes = self.FindClassnames(cls)
        ActionChains(self.driver).move_to_element(classes).perform()

        time.sleep(2)

    # 封装浮动时查找元素
    def ActionMove1(self,controls):
        ActionChains(self.driver).move_to_element(controls).perform()
        time.sleep(2)

    # 封装休眠方法，三种：1.静止休眠  2.隐式休眠  3.显式休眠
    def TimeSleep(self,number):
        time.sleep(number)

    def ImplicitySleep(self,number):
        self.driver.implicitly_wait(number)

    def WebwaitSleep(self,message):
        # 查找内容
        text = (By.LINK_TEXT,message)
        # 设置休眠时间
        WebDriverWait(self.driver,20,1).until(EC.presence_of_element_located(text))

    # # 封装查找控件方法1
    def Findid(self, id):
        time.sleep(2)
        return self.driver.find_element_by_id(id)

    # # 封装查找控件方法2
    def FindClassname(self,name):
        time.sleep(2)
        return self.driver.find_element_by_class_name(name)

    def FindClassnames(self,name):
        time.sleep(2)
        return self.driver.find_elements_by_class_name(name)

    # # 封装查找控件方法3
    def FindLinktext(self, text):
        time.sleep(2)
        return self.driver.find_element_by_link_text(text)

    # # 封装查找控件方法4
    def FindXpath(self, xpath):
        time.sleep(2)
        return self.driver.find_element_by_xpath(xpath)

    # # 封装查找控件方法5
    def FindTagname(self, tagname):
        time.sleep(2)
        return self.driver.find_element_by_tag_name(id)

    # # 封装查找控件方法6
    def FindCss(self, css):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(css)

    # # 封装查找控件方法7
    def FindPart(self, partial):
        time.sleep(2)
        return self.driver.find_element_by_partial_link_text(partial)

    # # 封装查找控件方法8
    def FindName(self, name):
        time.sleep(2)
        return self.driver.find_element_by_name(name)

    # # 封装查找控件方法1
    # def FindIDs(self,ID):
    #
    #     try:
    #         # 查找内容
    #         ids = (By.ID,ID)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(ids))
    #         return self.driver.find_elements_by_id(ID)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法2
    # def FindNames(self, name):
    #
    #     try:
    #         # 查找内容
    #         names = (By.NAME, name)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(names))
    #         return self.driver.find_elements_by_name(names)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法3
    # def FindClassNames(self, class_name):
    #
    #     try:
    #         # 查找内容
    #         class_names = (By.CLASS_NAME, class_name)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(class_names))
    #         return self.driver.find_elements_by_class_name(class_name)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法4
    # def FindXpaths(self, xpath):
    #
    #     try:
    #         # 查找内容
    #         xpaths = (By.XPATH, xpath)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(xpaths))
    #         return self.driver.find_elements_by_xpath(xpath)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法5
    # def FindLinkTexts(self, link_text):
    #
    #     try:
    #         # 查找内容
    #         link_texts = (By.LINK_TEXT, link_text)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(link_texts))
    #         return self.driver.find_elements_by_link_text(link_text)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法6
    # def FindTagNames(self, tag_name):
    #
    #     try:
    #         # 查找内容
    #         tag_names = (By.TAG_NAME, tag_name)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(tag_names))
    #         return self.driver.find_elements_by_tag_name(tag_name)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法7
    # def FindPartials(self, partial):
    #
    #     try:
    #         # 查找内容
    #         partials = (By.PARTIAL_LINK_TEXT, partial)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(partials))
    #         return self.driver.find_elements_by_partial_link_text(partial)
    #     except Exception:
    #         pass
    #
    # # 封装查找控件方法8
    # def FindCsses(self, css):
    #
    #     try:
    #         # 查找内容
    #         css = (By.CSS_SELECTOR, css)
    #         # 设置休眠时间
    #         WebDriverWait(self.driver, 20, 1).until(
    #             EC.presence_of_element_located(css))
    #         return self.driver.find_elements_by_css_selector(css)
    #     except Exception:
    #         pass


