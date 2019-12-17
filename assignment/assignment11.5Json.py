# https://www.py4e.com/tools/python-data/?PHPSESSID=06dc5e76c79f914c7440b99e31f59c8b
# https://www.coursera.org/learn/python-network-data/gradedLti/uKuU0/extracting-data-from-json

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_332124.json'
data = urllib.request.urlopen(url, context=ctx).read()
result = json.loads(data)

print(' result:', len(result))
sum = 0

for item in result["comments"]:
    print('Name', item['name'])
    print('count', item['count'])
    sum = sum + int(item['count'])
print(sum) 