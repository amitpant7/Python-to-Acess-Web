import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input("Enter Location:")
# url = "http://py4e-data.dr-chuck.net/comments_42.xml"
fhand= urllib.request.urlopen(url)
print("Retrieving http://py4e-data.dr-chuck.net/comments_42.xml")
data=fhand.read()
datalen = len(data)
print( "Retriving", datalen, "Characters"  )
#print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
i=0 
sum= 0
for item in lst:
    count= item.find('count')
    sum= sum+int(count.text)
    i= i+1
print("Count:", i)
print("The Sum: ", sum)

