# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re

pattern = re.compile(r'\[em\](.*)\[\\/em\]')
s = '帮闺蜜转下，挣钱了带我去装逼[em]e113[\/em][em]e113[\/em]需要的微信私聊即可'
print re.sub(pattern, '', s)

# match1 = pattern.match('hello world!')
# match2 = pattern.match('helloo world!')
# match3 = pattern.match('helllo world!')

# if match1:
#     print match1.group()
# else:
#     print 'match1 匹配失败！'

# if match2:
#     print match2.group()
# else:
#     print 'match2 匹配失败！'

# if match3:
#     print match3.group()
# else:
#     print 'match3 匹配失败！'
    
