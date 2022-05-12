import urllib.request , urllib.parse , urllib.error
import json 

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
while True:
    address = input("Enter Address:")
    url= serviceurl+urllib.parse.urlencode({'address': address})
    print("Retriving Url:", url)
    fh = urllib.request.urlopen(url)
    data = fh.read()
    print(data)