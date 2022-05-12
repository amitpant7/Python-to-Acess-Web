import urllib.request, urllib.error, urllib.parse
import ssl
from bs4 import BeautifulSoup 
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand = urllib.request.urlopen('https://merolagani.com/LatestMarket.aspx')
data = fhand.read()
soup = BeautifulSoup(data, 'lxml')

#Scraping Data
tags = soup('tr')
#name= input("Enter Company symbol:")
fwrite= open('Content.txt','w')
for tag in tags:
    link = soup('a')
    #print('Contents:', tag.contents[0])
    fwrite.write(str(tag))
    fwrite.write('\n')
    
fwrite.close()