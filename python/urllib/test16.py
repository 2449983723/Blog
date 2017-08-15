import os
import shutil
import urllib
import urllib2
import requests

url = 'http://avatar.csdn.net/blogpic/20120328224350711.jpg'
savepath = 'downloads/test2.jpg'

if os.path.isdir('downloads'):
    shutil.rmtree('downloads')
if not os.path.isdir('downloads'):
    os.makedirs('downloads')

urllib.urlretrieve(url, savepath)
