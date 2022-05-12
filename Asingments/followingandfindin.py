import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#Scraping the page 
url = input("Enter the url:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

pos= int(input("Enter the Position :"))
i = int(input("Enter the number of times to repeat:"))

#Extracting the anchor tag
n=0
while(n<i): 
    tags = soup('a')
    links =list()
    name= list()
    for tag in tags:
        link= tag.get('href', None)
        anchor=tag.contents[0]
        name.append(anchor)
        links.append(link)
    url= str(links[pos-1])
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    n=n+1
    print(url)
    print(name[pos-1])


