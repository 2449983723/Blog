import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = 'src="http://.*\.gif"'
    print (html)
    imglist = re.findall(reg, html)
    for i in range(0, len(imglist)):
        print(imglist[i])
        urllib.urlretrieve(imglist[i], str(i + 1) + '.gif')

string = raw_input('Please input URL:')
html = getHtml(string)
getImg(html)
print 'Finish!'

