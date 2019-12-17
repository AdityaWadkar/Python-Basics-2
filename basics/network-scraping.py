## Scraping Libary
## Beautifull soup: https://pypi.org/project/beautifulsoup4/
## Lession Video: https://www.coursera.org/learn/python-network-data/lecture/1oHBS/12-5-parsing-web-pages

# To run this, download the BeautifulSoup zip file
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://de.wikipedia.org/wiki/Las_Vegas'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
