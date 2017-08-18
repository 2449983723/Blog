import re

p = re.compile(r'(\w_) (\w+)(?P<sign>.*)', re.DOTALL)

print 'p.pattern:', p.pattern
print 'p.fla'