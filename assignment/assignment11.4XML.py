# https://www.py4e.com/tools/python-data/?PHPSESSID=05eecfe2cbdb2fe855f4007185a22a86

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_332123.xml'
xmls = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xmls)

lst = tree.findall('comments/comment')
print('User count:', len(lst))

sum = 0

for item in lst:
    print('Name', item.find('name').text)
    print('count', item.find('count').text)
    sum = sum + int(item.find('count').text)
print("Sum:", sum)
    