import urllib
import urllib2

url = 'http://run.hbut.edu.cn/Account/LogOn'

response = urllib2.urlopen(url)
html = response.read()
print html