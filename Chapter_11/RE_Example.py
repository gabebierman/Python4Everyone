from pickletools import int4
import re

sum = 0
hand = open('Actual.txt')

for line in hand :
    
    stuff = re.findall('[0-9]+' , line)
    for integer in stuff :
        sum = sum + float(integer)
    #print(stuff)
print('Sum: ', sum)