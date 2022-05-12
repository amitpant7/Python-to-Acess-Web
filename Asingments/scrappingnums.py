import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
#scrapping the page
page = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1390766.html').read()
data = BeautifulSoup(page, 'html.parser')

#Extracting numbers, we will extrat out the <span> tag

numbers = list()
tags = data('span')
for tag in tags:
    nums = tag.contents[0]
    print(nums)

#The other Way 
# strtag= str(tags)
# nums= re.findall('[0-9]+',strtag)

# #calculating Sum
# sum=0
# for num in nums:
#     sum = sum+int(num)
# print(sum)