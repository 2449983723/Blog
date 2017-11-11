#coding:utf8
import threading
from time import ctime,sleep
from test.xiaohua import multiThreadingGet

# def music(func):
#     for i in range(2):
#         print "I was listening to %s. %s" %(func,ctime())
#         sleep(1)

# def movie(func):
#     for i in range(2):
#         print "I was at the %s! %s" %(func,ctime())
#         sleep(5)


# threads = []
# threadMusic = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(threadMusic)
# threadMovie = threading.Thread(target=movie,args=(u'阿凡达',))
# threads.append(threadMovie)

if __name__ == '__main__':
    thumbUpCount = int(raw_input(u'请输入笑话的好笑程度（表示有多少人点赞）：'))
    multiThreadingGet(thumbUpCount, 3)
    # for td in threads:
    #     td.setDaemon(True)
    #     td.start()

    # td.join()
    # print "all over %s" %ctime()