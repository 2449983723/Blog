#coding=utf-8
import requests
import re
import datetime
import MySQLdb
import csv
import traceback
from selenium import webdriver
from time import sleep
import json
import sys
import warnings
warnings.filterwarnings("ignore") #忽略警告输出
reload(sys)
sys.setdefaultencoding("utf-8")


class QQMood:
    cookie = None
    gtk = None
    qzonetoken = None
    db_conn = None
    db_cursor = None
    request_session = None
    friends = None
    qq = None
    password = None

    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': '*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection':'keep-alive'
    }#伪造浏览器头

    # 启动抓取程序
    def start(self, qq, password):
        self.qq = qq
        self.password = password
        self.__login()
        self.__saveFriendsQQ()
        self.__connectMySql()
        self.__createDb()
        self.__createDbTable()
        self.__spideShuoShuo()
        self.__closeDbConnect()

    # 登录
    def __login(self):
        browser = webdriver.PhantomJS()#这里要输入你的phantomjs所在的路径
        url = "https://qzone.qq.com/"#QQ登录网址
        browser.get(url)
        browser.maximize_window()#全屏
        sleep(5)
        try:
            browser.find_element_by_id('login_div')
            a = True
        except:
            a = False
        if a == True:
            browser.switch_to.frame('login_frame')
            browser.find_element_by_id('switcher_plogin').click()
            browser.find_element_by_id('u').clear()#选择用户名框
            browser.find_element_by_id('u').send_keys(self.qq)
            browser.find_element_by_id('p').clear()
            browser.find_element_by_id('p').send_keys(self.password)
            browser.find_element_by_id('login_button').click()
        sleep(5)#等二十秒，可根据自己的网速和性能修改
        print(browser.title)#打印网页标题
        self.cookie = {} #初始化cookie字典
        for elem in browser.get_cookies():#取cookies
            self.cookie[elem['name']] = elem['value']
        print('Get the cookie of QQlogin successfully!(共%d个键值对)' % (len(self.cookie)))
        html = browser.page_source #保存网页源码
        g_qzonetoken = re.search(r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',html) #从网页源码中提取g_qzonetoken
        self.gtk = self.__getGTK()#通过getGTK函数计算gtk
        self.qzonetoken = g_qzonetoken.group(1)
        self.request_session = requests.session()#用requests初始化会话
        browser.quit()

    # 保存好友列表
    def __saveFriendsQQ(self):
        friends_url = 'http://m.qzone.com/friend/mfriend_list'
        params={
            'res_uin':'2449983723',
            'res_type':'normal',
            'format':'json',
            'count_per_page':'10',
            'page_index':'0',
            'page_type':'0',
            'g_tk':str(self.gtk),
            'mayknowuin':'',
            'qqmailstat':'',
        }
        response = self.request_session.request('GET',friends_url, params=params, headers=self.headers, cookies=self.cookie)
        print(response.status_code)#通过打印状态码判断是否请求成功
        friend_json_object = json.loads(response.text)  # json字符串转字典 
        if friend_json_object['code'] == -3000:
            print friend_json_object['message']
        else:
            self.friends = []
            items_list = friend_json_object['data']['list']
            for item in items_list:
                self.friends.append(str(item['uin']).rstrip().strip())


    #连接数据库
    def __connectMySql(self):
        self.db_conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306, charset="utf8", use_unicode=True)
        self.db_cur = self.db_conn.cursor()
       
    #创建数据库
    def __createDb(self):
        database_name = 'qq_mood'
        self.db_cur.execute('create database if not exists ' + database_name)
        self.db_conn.select_db(database_name)

    #创建数据库表
    def __createDbTable(self):
        # 创建数据表SQL语句
        create_table_sql = '''create table if not exists mood (id varchar(500),qq varchar(500),content varchar(10000),time varchar(500),sitename varchar(500),pox_x varchar(500),pox_y varchar(500),tool varchar(500),comments_num varchar(500),date varchar(500),isTransfered varchar(500),name varchar(500), PRIMARY KEY (id))'''
        self.db_cur.execute(create_table_sql)

    # 关闭数据库连接
    def __closeDbConnect(self):
        self.db_cur.close()
        self.db_conn.close()

    # 爬取说说
    def __spideShuoShuo(self):
        emoji_pattern = re.compile(r'\[em\](.*)\[\\/em\]')

        for qq in self.friends:#遍历qq号列表
            for p in range(0,1000):
                pos=p*20
                params={
                'uin':qq,
                'ftype':'0',
                'sort':'0',
                'pos':pos,
                'num':'20',
                'replynum':'100',
                'g_tk':self.gtk,
                'callback':'_preloadCallback',
                'code_version':'1',
                'format':'jsonp',
                'need_private_comment':'1',
                'qzonetoken':self.qzonetoken
                }

                response = self.request_session.request('GET','https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6',params=params,headers=self.headers,cookies=self.cookie)
                print(response.status_code)#通过打印状态码判断是否请求成功
                if (response.status_code == 200):
                    text = response.text#读取响应内容
                    if not re.search('lbs', text):#通过lbs判断此qq的说说是否爬取完毕
                        print('%s说说下载完成'% qq)
                        break
                    textlist = re.split('\{"certified"', text)[1:]
                    for ss_item in textlist:
                        myMood = self.__parse_mood(ss_item, qq)
                        '''将提取的字段值插入mysql数据库，通过用异常处理防止个别的小bug中断爬虫，开始的时候可以先不用异常处理判断是否能正常插入数据库'''
                        try:
                            insert_sql = '''replace into mood(id,qq,content,time,sitename,pox_x,pox_y,tool,comments_num,date,isTransfered,name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                            self.db_cur.execute(insert_sql, (myMood['id'],myMood['qq'],myMood["Mood_cont"],myMood['time'],myMood['idneme'],myMood['pos_x'],myMood['pos_y'],myMood['tool'],myMood['cmtnum'],myMood['date'],myMood["isTransfered"],myMood['name']))
                            self.db_conn.commit()
                            # dumpToFile(myMood['date'] + ' ' + myMood['time'] + '   ' + myMood['tool'] + '  ' + myMood['id'])
                            # dumpToFile('\n')
                            # dumpToFile(re.sub(emoji_pattern, '', myMood['Mood_cont']))
                            # dumpToFile('\n\n')
                        except Exception as e:
                            print ss_item
                            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            print('说说全部下载完成！')
    
    # 解析获得gtk
    def __getGTK(self):
        """ 根据cookie得到GTK """
        hashes = 5381
        for letter in self.cookie['p_skey']:
            hashes += (hashes << 5) + ord(letter)
        return hashes & 0x7fffffff

    # 解析单条说说内容
    def __parse_mood(self, ss_item, qq):
        '''从返回的json中，提取我们想要的字段'''
        text = re.sub('"commentlist":.*?"conlist":', '', ss_item)
        if text:
            myMood = {}
            myMood["isTransfered"] = False
            tid = re.findall('"t1_termtype":.*?"tid":"(.*?)"', text)[0]  # 获取说说ID
            tid = qq + '_' + tid
            myMood['id'] = tid
            myMood['qq'] = qq
            myMood['pos_y'] = 0
            myMood['pos_x'] = 0
            mood_cont = re.findall('\],"content":"(.*?)"', text)
            if re.findall('},"name":"(.*?)",', text):
                name = re.findall('},"name":"(.*?)",', text)[0]
                myMood['name'] = name
            if len(mood_cont) == 2:  # 如果长度为2则判断为属于转载
                myMood["Mood_cont"] = "评语:" + mood_cont[0] + "--------->转载内容:" + mood_cont[1]  # 说说内容
                # myMood["Mood_cont"] = mood_cont[0]
                myMood["isTransfered"] = True
            elif len(mood_cont) == 1:
                myMood["Mood_cont"] = mood_cont[0]
            else:
                myMood["Mood_cont"] = ""
            if re.findall('"created_time":(\d+)', text):
                created_time = re.findall('"created_time":(\d+)', text)[0]
                temp_pubTime = datetime.datetime.fromtimestamp(int(created_time))
                temp_pubTime = temp_pubTime.strftime("%Y-%m-%d %H:%M:%S")
                dt = temp_pubTime.split(' ')
                time = dt[1]
                myMood['time'] = time
                date = dt[0]
                myMood['date'] = date
            if re.findall('"source_name":"(.*?)"', text):
                source_name = re.findall('"source_name":"(.*?)"', text)[0]  # 获取发表的工具（如某手机）
                myMood['tool'] = source_name
            if re.findall('"pos_x":"(.*?)"', text):
                pos_x = re.findall('"pos_x":"(.*?)"', text)[0]
                pos_y = re.findall('"pos_y":"(.*?)"', text)[0]
                if pos_x:
                    myMood['pos_x'] = pos_x
                if pos_y:
                    myMood['pos_y'] = pos_y
                idname = re.findall('"idname":"(.*?)"', text)[0]
                myMood['idneme'] = idname
                cmtnum = re.findall('"cmtnum":(.*?),', text)[0]
                myMood['cmtnum'] = cmtnum
            return myMood


    #清空文件内容
    def __clearFile(self, file_name):
        f = open(file_name, 'w+')
        f.truncate()
        f.close()

    # 输出内容到文件
    def __dumpToFile(self, file_name, content):
        f = open(file_name, 'a')
        f.write(content)
        f.close()

qqMood = QQMood()
qqMood.start('2449983723', 'Ln@hbutrj1b')