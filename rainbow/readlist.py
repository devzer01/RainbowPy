'''
Created on Jul 8, 2013

@author: nayanahettiarachchi

http://www.rainbowpages.lk/_controller/searchcontroller.php?action=AdvPersonalSearch
post personal_quick_keyword=de silva

redirect to http://www.rainbowpages.lk/personal-name-search-result.php

'''
from xml.dom.minidom import parse, parseString
import urllib2
from bs4 import BeautifulSoup

url = "http://www.rainbowpages.lk/_controller/searchcontroller.php?action=AdvPersonalSearch"
resp = urllib2.urlopen(url, "personal_quick_keyword=de silva", 200)
cookie = resp.headers.get('Set-Cookie')

out = urllib2.Request("http://www.rainbowpages.lk/personal-name-search-result.php")
out.add_header('cookie', cookie)
response = urllib2.urlopen(out)

document = ""

for line in response.readlines():
    document += line


soup = BeautifulSoup(document)

table = soup.find('div', attrs={"class":"content-details"}).findNext("table")

print table
