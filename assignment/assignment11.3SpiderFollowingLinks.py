# https://www.py4e.com/tools/python-data/?PHPSESSID=9e65d0aedc310d7251fb8ba246b3792b


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


repeat = 7
position = 18

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [] 
urls.append('http://py4e-data.dr-chuck.net/known_by_Naina.html')

i = 0

while i < repeat + 1:   

    html = urlopen(urls[i], context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')

    urls.append(tags[position -1].get('href', None))
    print(urls[i])
    ##Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    i = i + 1

