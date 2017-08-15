#!/usr/bin/env python
#coding=utf8

import WeiboCrawl

if __name__ == '__main__':
    weiboLogin = WeiboCrawl.WeiboLogin('15201397022', '2449983723')
    if weiboLogin.Login() == True:
        print "The WeiboLogin module works well!"

    #start with my blog :)
    webCrawl = WeiboCrawl.WebCrawl('http://weibo.com/yaochen')
    webCrawl.Crawl()
    del webCrawl