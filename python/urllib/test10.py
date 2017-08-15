import urllib2
html = urllib2.urlopen('http://user.qzone.qq.com/2449983723?ptsig=hpr3DWzqFoNSEvdS2-3K0S2RbMfV1tsDN-Hvu0OWpJ8_').read()
print 'size is', len(html)
print html