# import re
#
# str='class will start at 10 am'
# s = re.search('\s',str)
# print(s)
# print(s.start())
#
# s1 = re.search('\d',str)
# print(s1)
#
# s2 = re.search('python',str)
# print(s2)
import re

str2 = 'class will start at 10 am'
s = re.search('^class.*10am$',str2)
print(s)
if s:
    print('find')
else:
    print('not find')