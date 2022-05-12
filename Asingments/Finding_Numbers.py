#l read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re
file= open("regex_sum.txt", 'r')
data = file.read()
num = re.findall('[0-9]+', data)
#print(num)
file.close()
file = open("num.txt", "w")
for n in num:
    file.write(n)
    file.write('\n')
file.close()
file = open("num.txt","r" )
sum =0 
for line in file:
    sum = sum+ int(line)
print(sum)
file.close()