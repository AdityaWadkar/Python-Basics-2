# import re
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@(\S+)' , x)
# print(y)
# print('--------------------')

# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)
# print('--------------------')

# import re
# x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('\S+?@\S+' , x)
# print(y)
# print('--------------------')


import re
x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('href=(.+)' , x)
print(y)
print('--------------------')
