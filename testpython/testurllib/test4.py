from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://rrurl.cn/b1UZuP'
req = Request(old_url)
response = urlopen(req)
the_page = response.read()
print 'Old url:' + old_url
print 'Real url:' + response.geturl()
print 'The Page:' + the_page