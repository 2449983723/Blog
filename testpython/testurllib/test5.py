from urllib2 import Request, urlopen, URLError, HTTPError

url = 'http://www.baidu.com'
req = Request(url)
response = urlopen(req)

print 'Info:'
print response.info()