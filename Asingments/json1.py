import urllib.request, urllib.parse, urllib.error
import json

loc = input("Enter the Location:")
print("Retriving ..", loc)
fh = urllib.request.urlopen(loc)
data = fh.read()
lenght = len(data)
print("Retrived", lenght, "characters")
info = json.loads(data)
infolist = info["comments"]
count = len(infolist)
sum = 0
for item in infolist:
    sum= sum+ int(item["count"])
    
print("Count:", count)
print("Sum:", sum)