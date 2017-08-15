# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re

match = re.match(r'\d+?','102300')

if match:
    print match.group()
else:
    print ('匹配失败！')