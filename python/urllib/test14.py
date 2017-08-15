# import re
# p = re.compile('ab*', re.IGNORECASE)
# print p

import re
p = re.compile('[a-z]+')
m = p.match('dlfj')
print m.group()
print m.start()
print m.end()
print m.span()