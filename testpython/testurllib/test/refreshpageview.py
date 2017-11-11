# coding=utf-8
import string, urllib2, re

import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")


def tiquneirong(pageUrl, refreshCount):
    index = 0
    pageIndex = 1

    #下载页面
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    while pageIndex <= refreshCount:
        try:
            req = urllib2.Request(pageUrl, headers = headers)
            curPage = urllib2.urlopen(req).read()
            print '刷新次数' + str(pageIndex)
            pageIndex = pageIndex + 1
            # time.sleep(1)
        except Exception, e:
            print 'e.message:\t', e.message

tiquneirong("http://blog.csdn.net/xiao_nian/article/details/58596215", 10000)
        