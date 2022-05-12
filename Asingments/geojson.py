import urllib.request, urllib.parse, urllib.error
import json ,ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urldef= "http://py4e-data.dr-chuck.net/json?"
address = input("Enter Address:")

#dictionary for api key parameter
par= dict() 
par["address"]= address
par["key"]= 42

#Getting the Url
url = urldef+ urllib.parse.urlencode(par)
print("Retriving ", url)
fh =urllib.request.urlopen(url)
data= fh.read()
info = json.loads(data)
print("Place ID:",info["results"][0]["place_id"])
