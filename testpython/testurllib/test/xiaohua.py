# coding=utf-8
import string, urllib2, re

import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")

# def qiushibaike(url, begin_page, end_page):
#     for i in range(begin_page, end_page + 1):
#         sName = str(i) + '.html'
#         print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
#         f = open('data/' + sName, 'w+')

#         user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         headers = { 'User-Agent' : user_agent }
#         req = urllib2.Request(url + str(i), headers = headers)
#         curPage = urllib2.urlopen(req).read()

#         f.write(curPage)
#         f.close()

# def tiquneirong(begin_page, end_page):
#     print "\n\n"
#     for i in range(begin_page, end_page + 1):
#         print "第" + str(i) + "页的内容\n"
#         sName = str(i) + '.html'
#         file_object = open('data/' + sName)
#         try:
#             myPage = file_object.read()
#         finally:
#             file_object.close()

#         # 找出所有class="content"的div标记
#         #re.S是任意匹配模式，也就是.可以匹配换行符
#         myItems = re.findall('<div class="content">(\s*)(.*?)(<!--.*?-->.*?)</div>', myPage, re.S)
#         j = 0
#         for item in myItems:
#             j = j + 1
#             print str(j) + '、'
#             print item[1].replace("<br/>", "\n")

# def tiquneirong(begin_page, end_page):
#     for i in range(begin_page, end_page + 1):

#         #下载页面
#         user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         headers = { 'User-Agent' : user_agent }
#         req = urllib2.Request(qsurl + str(i), headers = headers)
#         curPage = urllib2.urlopen(req).read()

#         print "第" + str(i) + "页的内容\n"
#         #从页面提取内容并输出
#         #找出所有class="content"的div标记
#         #re.S是任意匹配模式，也就是.可以匹配换行符
#         myItems = re.findall('<a href="/users/(.*?)title="(.*?)">(.*?)<div class="content">(\s*)(.*?)<!--(.*?)<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>', curPage, re.S)
#         j = 0
#         for item in myItems:
#             author = item[1]
#             content = item[4].replace("<br/>", "\n")
#             thumbUpCount = int(item[6])
#             if(len(content) > 100) and (thumbUpCount > 10000):
#                 j = j + 1
#                 print str(j) + '、' + '作者：' + author + ' 好笑:' + str(thumbUpCount)
#                 print content
#         print "\n\n"
# qsurl = 'http://www.qiushibaike.com/hot/page/'
# begin_page = int(raw_input(u'请输入开始页数：'))
# end_page = int(raw_input(u'请输入终止页数：'))

# def tiquneirong(count, thumbUpCount):
#     j = 0
#     perform = False
#     #最多只获取前1000页的内容
#     for i in range(1, 200 + 1):
#         #下载页面
#         user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         headers = { 'User-Agent' : user_agent }
#         req = urllib2.Request(qsurl + str(i), headers = headers)
#         curPage = urllib2.urlopen(req).read()

#         #从页面提取内容并输出
#         #找出所有class="content"的div标记
#         #re.S是任意匹配模式，也就是.可以匹配换行符
#         myItems = re.findall('<a href="/users/(.*?)title="(.*?)">(.*?)<div class="content">(\s*)(.*?)<!--(.*?)<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>', curPage, re.S)
#         for item in myItems:
#             author = item[1]
#             content = item[4].replace("<br/>", "\n")
#             curThumbUpCount = int(item[6])
#             if(len(content) > 120) and (curThumbUpCount > thumbUpCount):
#                 j = j + 1
#                 print str(j) + '、' + '作者：' + author + ' 好笑:' + str(curThumbUpCount)
#                 print content
#             if(j >= count):
#                 perform = True
#                 break

#         if(perform):
#             break

#     print "\n\n"
# qsurl = 'http://www.qiushibaike.com/hot/page/'
# count = int(raw_input(u'请输入要获取的笑话的个数：'))
# thumbUpCount = int(raw_input(u'请输入笑话的好笑程度（表示有多少人点赞）：'))

# tiquneirong(count, thumbUpCount)

def tiquneirong(thumbUpCount):
    qsurl = 'http://www.qiushibaike.com/hot/page/'
    index = 0
    pageIndex = 1

    myInput = raw_input(u'按回车加载笑话内容...')
    if(myInput == 'q'):
        return
    print '正在加载，请稍等...'
    #下载页面
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    while pageIndex <= 200:
        print qsurl + str(pageIndex)
        req = urllib2.Request(qsurl + str(pageIndex), headers = headers)
        curPage = urllib2.urlopen(req).read()

        #从页面提取内容并输出
        #找出所有class="content"的div标记
        #re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall('<a href="/users/(.*?)<h2>(\s*)(.*?)(\s*)</h2>(.*?)<div class="content">(\s*)<span>(\s*)(.*?)(\s*)</span>(.*?)<!--(.*?)<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>', curPage, re.S)
        for item in myItems:
            author = item[2]
            content = item[7].replace("<br/>", "\n")
            curThumbUpCount = int(item[11])
            if(len(content) > 100) and (curThumbUpCount > thumbUpCount):
                index = index + 1
                print str(index) + '、' + '作者：' + author + ' 好笑:' + str(curThumbUpCount)
                print content + "\n"

            if(index != 0 and index%5 == 0):
                myInput = raw_input()
                while myInput != '':
                    if(myInput == 'q'):
                        return
                    myInput = raw_input()
                print '正在加载，请稍等...'

        pageIndex = pageIndex + 1
        time.sleep(1)
        
    print "\n\n"

def gettiquneirong(thumbUpCount, xiaohuaCount):
    qsurl = 'http://www.qiushibaike.com/hot/page/'
    pageIndex = 1

    #下载页面
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    result = ''
    xiaohuaNum = 0
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    while pageIndex <= 200 and xiaohuaNum < xiaohuaCount:
        req = urllib2.Request(qsurl + str(pageIndex), headers = headers)
        curPage = urllib2.urlopen(req).read()

        #从页面提取内容并输出
        #找出所有class="content"的div标记
        #re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall('<a href="/users/(.*?)<h2>(\s*)(.*?)(\s*)</h2>(.*?)<div class="content">(\s*)<span>(\s*)(.*?)(\s*)</span>(.*?)<!--(.*?)<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>', curPage, re.S)
        for item in myItems:
            author = item[2]
            content = item[7].replace("<br/>", "\n")
            curThumbUpCount = int(item[11])
            if (xiaohuaNum >= xiaohuaCount):
                break
            if (len(content) > 100) and (curThumbUpCount > thumbUpCount):
                result = result + str(xiaohuaNum + 1) + '、' + '\n'
                result = result + content + "\n\n"
                xiaohuaNum = xiaohuaNum + 1
        pageIndex = pageIndex + 1
        time.sleep(1)


    return result

# def tiquneirong(tiebaUrl):
#     index = 0
#     pageIndex = 1
#     pageCount = 10000
#     title = "noTitle"
#     fileWriter = 0

#     #下载页面
#     user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#     headers = { 'User-Agent' : user_agent }
#     aPatternContent = re.compile('(.*?)<a href=(.*?)>(.*?)</a>(.*)')
#     imgPatternContent = re.compile('(.*?)<img(.*?)>(.*?)')



#     while pageIndex <= pageCount:
#         req = urllib2.Request(tiebaUrl + str(pageIndex), headers = headers)
#         curPage = urllib2.urlopen(req).read()

#         # 从页面提取内容并输出
#         # 找出所有class="content"的div标记
#         # re.S是任意匹配模式，也就是.可以匹配换行符


#         if(pageCount == 10000):
#             #找到总共有多少页
#             pageCountMatch = re.search(r'class="red">(\d+?)</span>', curPage, re.S)
#             if pageCountMatch:
#                 pageCount = int(pageCountMatch.group(1))
#                 print u'爬虫报告：发现楼主共有%d页的原创内容' % pageCount
#             else:
#                 pageCount = 0
#                 print u'爬虫报告：无法计算楼主发布内容有多少页！'
#                 return
#             #找到标题
#             pageTitleMatch = re.search(r'<title>(.*?)</title>', curPage, re.S)
#             if pageTitleMatch:
#                 title = pageTitleMatch.group(1)

#             # fileWriter = open('data/' + title + ".txt", 'w+')


#         #解析页面内容
#         myItems = re.findall('class="d_post_content j_d_post_content ">(.*?)</div>', curPage, re.S)
#         for item in myItems:
#             content = item.replace("<br>", "\n").replace("</br>", "\n")
#             isOk = False
#             while isOk == False:
#                 contentMatch = re.search(aPatternContent, content)
#                 if contentMatch:
#                     content = contentMatch.group(1) + contentMatch.group(3) + contentMatch.group(4)
#                 else:
#                     isOk = True

#             isOk = False
#             while isOk == False:
#                 contentMatch = re.search(imgPatternContent, content)
#                 if contentMatch:
#                     content = contentMatch.group(1) + contentMatch.group(3)
#                 else:
#                     isOk = True

#             content = re.sub(r'\s+', '', content)
#             print "    " + content
#             print "\n"
#             # fileWriter.write("    " + content + "\n")
#         pageIndex = pageIndex + 1
#     print "\n\n"

# tiebaUrl = raw_input(u'请输入文章的地址：')
# tiebaUrl = tiebaUrl + '?see_lz=1&pn='
# tiquneirong(tiebaUrl)

# def tiquneirong(tiebaUrl):
#     index = 0
#     pageIndex = 1
#     pageCount = 10000
#     title = "noTitle"
#     fileWriter = 0

#     #下载页面
#     user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#     headers = { 'User-Agent' : user_agent }
#     aPatternContent = re.compile('(.*?)<a href=(.*?)>(.*?)</a>(.*)')
#     imgPatternContent = re.compile('(.*?)<img(.*?)>(.*?)')



#     while pageIndex <= pageCount:
#         req = urllib2.Request(tiebaUrl + str(pageIndex), headers = headers)
#         curPage = urllib2.urlopen(req).read()

#         # 从页面提取内容并输出
#         # 找出所有class="content"的div标记
#         # re.S是任意匹配模式，也就是.可以匹配换行符


#         if(pageCount == 10000):
#             #找到总共有多少页
#             pageCountMatch = re.search(r'class="red">(\d+?)</span>', curPage, re.S)
#             if pageCountMatch:
#                 pageCount = int(pageCountMatch.group(1))
#                 print u'爬虫报告：发现楼主共有%d页的原创内容' % pageCount
#             else:
#                 pageCount = 0
#                 print u'爬虫报告：无法计算楼主发布内容有多少页！'
#                 return
#             #找到标题
#             pageTitleMatch = re.search(r'<title>(.*?)</title>', curPage, re.S)
#             if pageTitleMatch:
#                 title = pageTitleMatch.group(1)

#             # fileWriter = open('data/' + title + ".txt", 'w+')


#         #解析页面内容
#         myItems = re.findall('class="d_post_content j_d_post_content ">(.*?)</div>', curPage, re.S)
#         for item in myItems:
#             content = item.replace("<br>", "\n").replace("</br>", "\n")
#             isOk = False
#             while isOk == False:
#                 contentMatch = re.search(aPatternContent, content)
#                 if contentMatch:
#                     content = contentMatch.group(1) + contentMatch.group(3) + contentMatch.group(4)
#                 else:
#                     isOk = True

#             isOk = False
#             while isOk == False:
#                 contentMatch = re.search(imgPatternContent, content)
#                 if contentMatch:
#                     content = contentMatch.group(1) + contentMatch.group(3)
#                 else:
#                     isOk = True

#             content = re.sub(r'\s+', '', content)
#             print "    " + content
#             print "\n"
#             # fileWriter.write("    " + content + "\n")
#         pageIndex = pageIndex + 1
#     print "\n\n"

# tiebaUrl = raw_input(u'请输入文章的地址：')
# tiebaUrl = tiebaUrl + '?see_lz=1&pn='
# tiquneirong(tiebaUrl)
