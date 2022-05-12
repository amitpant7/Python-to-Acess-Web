import re
emails = list()
file = open('mbox-short.txt', 'r')
for line in file :
    y = re.findall('^From (\S+@\S+)', line)
    if len(y) == 1:
        emails.append(y)
print(emails)