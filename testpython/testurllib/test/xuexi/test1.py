import urllib2

# response = urllib2.urlopen('http://www.baidu.com')
# html = response.read()
# print html

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
html = response.read()
print html