# coding=utf-8
import os
import re

fileName = raw_input(u'：')
toFileName = raw_input(u'：')
if not os.path.exists(fileName): # 看一下这个文件是否存在
    print("no fileName")
    exit(-1)                         #不存在就退出

lines = open(fileName).readlines()  #打开文件，读入每一行
fp = open(toFileName, 'w')  #打开你要写得文件test2.txt
for s in lines:
# replace是替换，write是写入
    fp.write(s.replace('love', 'hate'))
fp.close()  # 关闭文件