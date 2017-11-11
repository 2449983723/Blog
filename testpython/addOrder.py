#coding:utf8
import random
import json,urllib2
import traceback
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}

def dump(content):
    print json.dumps(content).decode('unicode-escape')

def postReq(postUrl, postData):
    req = urllib2.Request(url=postUrl, data=json.dumps(postData), headers=header_dict)
    result = urllib2.urlopen(req).read()
    return json.loads(result)

def getReq(getUrl):
    req = urllib2.Request(url=getUrl)
    result = urllib2.urlopen(req).read()
    return json.loads(result)

def randomList(minNum, maxNum, count):
    numList = []
    n = minNum
    while n <= maxNum:
        numList.append(n)
        n = n + 1
    return random.sample(numList, count)

def getBetString(betList):
    betContent = ""
    n = 0
    while n<len(betList):
        num = betList[n]
        if num < 10:
            betContent = betContent + '0'
        betContent = betContent + str(num)
        if (n < (len(betList)-1)):
            betContent = betContent + ','
        n = n + 1
    return betContent

def randomOneBet():
    betContent = ""
    betContent = getBetString(randomList(1, 35, 5)) + '|' + getBetString(randomList(1, 12, 2))
    return betContent

# 登录
loginRes = postReq('http://192.168.74.173:8160/lotto/android/passport/login', {"userName":"哦哦哦哦咯了","password":"17179b55a3a138358620eaeb118341eaf11faf253847d9a8d847582c6c6df2974c12409e18e1974163f697b1571cb5f8cf08965a716eb5b5e1e03b66d3492fc2","platform":3})
token = loginRes["data"]["tk"]
dump(token)

#获得大乐透彩期信息
lotteryInfo = getReq('http://192.168.74.173:8160/lotto/android/dlt/info')
curIssue = lotteryInfo["data"]["lotteryIssueBase"]["curIssue"]["issueCode"]
dump(curIssue)

n = 0
while n<20:
    try:
        # 下单
        addOrderRes = postReq('http://192.168.74.173:8160/lotto/order/addOrder', {"buyScreen":"","buyType":1,"channelId":"4","isDltAdd":0,"lotteryCode":102,"lotteryIssue":curIssue,"multipleNum":1,"orderAmount":"2","orderDetailList":[{"amount":"2","buyNumber":1,"codeWay":1,"contentType":1,"lotteryChildCode":10201,"multiple":1,"planContent":randomOneBet()}],"platform":3,"tabType":0,"token":token})
        dump(addOrderRes)
        oc = addOrderRes["data"]["oc"]
        dump(oc)

        # 支付
        payRes = postReq('http://sit.m.2ncai.com/lotto/h5/payCenter/pay', {"channelId":"4","clientType":2,"platform":3,"balance":2,"buyType":"1","orderCode":oc,"returnUrl":"http://sit.m.2ncai.com/payresult.html","token":token})
        dump(payRes)
    except:
        print 'traceback.format_exc():\n%s' % traceback.format_exc()
    n = n + 1