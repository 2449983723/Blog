#coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import traceback
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def dumpToFile(content):
    f = open('log.txt', 'w+')
    f.write(str(content))
    f.close()

class Praise():
    def __init__(self,QQ,password):
        self.QQ=QQ  
        self.password=password  
        self.logs=""  
        self.praised_list = []  
        self.url="https://user.qzone.qq.com/"
  
    def login_qzone(self):  
        self.browser = webdriver.Firefox()  
        self.browser.maximize_window()  
        self.browser.get(self.url)  
        self.browser.switch_to.frame("login_frame")  
        self.browser.find_element_by_id("switcher_plogin").click()  
        self.browser.find_element_by_id("u").clear()  
        self.browser.find_element_by_id("u").send_keys(self.QQ)  
        self.browser.find_element_by_id("p").clear()  
        self.browser.find_element_by_id("p").send_keys(self.password)  
        self.browser.find_element_by_id("login_button").click()  
        time.sleep(5)
        print "登录成功"
        # 解决FireFox的登录成功后，直接访问新页面出现can't access dead object错误的方法链接：  
        # http://stackoverflow.com/questions/16396767/firefox-bug-with-selenium-cant-access-dead-object  
        # 通过下面这句解决，可能时因为上面switch_to到了login_frame，所以现在它是dead object  
        self.browser.switch_to.default_content()

    def run(self):
        print 'Current URL:', self.browser.current_url
        # see more  
        html = self.browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        i = 0
        for child in soup.select('#feed_friend_list'):
            dumpToFile(child)

def main():
    # QQ =raw_input(u"输入QQ号：")
    # password =raw_input(u"输入QQ密码：")
    QQ = '2449983723'
    password = 'Ln@hbutrj1b'
    praise_spider = Praise(QQ,password)
    praise_spider.login_qzone()
    praise_spider.run()

if __name__ == "__main__":
    main()