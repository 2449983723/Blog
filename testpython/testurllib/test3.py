import urllib2

req = urllib2.Request('http://www.baidjf.com')

try: urllib2.urlopen(req)

except urllib2.URLError, e:
    print e.reason