import urllib.request, urllib.parse, urllib.error 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #Retuns the file handel 

# data = fhand.read()

for line in fhand:
    print(line.decode().strip())

