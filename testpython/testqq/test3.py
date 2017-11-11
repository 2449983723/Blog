#coding=utf-8
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def dumpToFile(content):
    f = open('test3log.txt', 'w+')
    f.write(str(content))
    f.close()

driver = webdriver.PhantomJS()
driver.get('http://hotel.qunar.com/city/beijing_city/dt-20438/?in_track=hotel_recom_beijing_city02')
data = driver.page_source
dumpToFile(data)
driver.quit()