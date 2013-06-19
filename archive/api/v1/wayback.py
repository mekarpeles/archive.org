import re
import requests
from BeautifulSoup import BeautifulSoup

archiveorg = 'http://web.archive.org'
wburl = archiveorg + '/web/*/'

def timeline(query):
    r = requests.get(wburl + query)
    soup = BeautifulSoup(r.content)
    img = soup.findAll('img', {'id': 'sparklineImgId'})[0]['src']
    return archiveorg + img

