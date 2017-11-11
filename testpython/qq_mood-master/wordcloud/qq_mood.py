#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image
import re
import MySQLdb
import traceback
import sys
import warnings
warnings.filterwarnings("ignore") #忽略警告输出
reload(sys)
sys.setdefaultencoding("utf-8")


class WordGenerater:
    db_conn = None
    db_cursor = None

    def __init__(self):
        self.__connectMySql()

    #连接数据库
    def __connectMySql(self):
        self.db_conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306, charset="utf8", use_unicode=True)
        self.db_cursor = self.db_conn.cursor()
        self.db_conn.select_db('qq_mood')

    # 关闭数据库连接
    def closeDbConnect(self):
        self.db_cursor.close()
        self.db_conn.close()

    def __getContentByQQ(self, qq):
        emoji_pattern = re.compile(r'\[em\](.*)\[\\/em\]')
        english_pattern = re.compile(r'\w')
        content = ''
        try:
            query_sql = "SELECT content from mood WHERE qq=%s" % (qq)
            self.db_cursor.execute(query_sql)
            # 获取所有记录列表
            results = self.db_cursor.fetchall()
            for row in results:
                content = content + re.sub(english_pattern, '', re.sub(emoji_pattern, '', row[0]))
        except:
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
        return content

    def genereteWordImg(self, qq):
        #读入背景图片
        abel_mask = np.array(Image.open("qq.jpg"))

        #通过jieba分词进行分词并通过空格分隔
        wordlist_after_jieba = jieba.cut(self.__getContentByQQ(qq), cut_all = True)
        stopwords = {u'转载', u'内容', 'em', u'评语', 'uin', 'nick'}

        seg_list = [i for i in wordlist_after_jieba if i not in stopwords]
        wl_space_split = " ".join(seg_list)
        #my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
        my_wordcloud = WordCloud(
                    background_color='black', # 设置背景颜色
                    mask = abel_mask,        # 设置背景图片
                    max_words = 50,            # 设置最大现实的字数
                    stopwords = STOPWORDS,        # 设置停用词
                    font_path = 'C:/Windows/Fonts/simkai.ttf',# 设置字体格式，如不设置显示不了中文
                    max_font_size = 80,            # 设置字体最大值
                    random_state = 40,            # 设置有多少种随机生成状态，即有多少种配色方案
                    scale=1.5,
                    relative_scaling=0.6
                    ).generate(wl_space_split)

        my_wordcloud.to_file(qq + ".jpg")

wordGenerater = WordGenerater()
wordGenerater.genereteWordImg('1095948418')
wordGenerater.closeDbConnect()