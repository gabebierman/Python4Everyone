#7.2 Write a program that prompts for a file name,
#  then opens that file and reads through the file,
#  looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point 
# values from each of the lines and compute the 
# average of those values and produce an output as
#  shown below. Do not use the sum() function or a
#  variable named sum in your solution.

# Use the file name mbox-short.txt as the file name

#extract all data after : and convert to float
#add all together and divide by count


count = 0                                  
total = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos+1:].strip()   
        SPAM_C = float(number)
        total = total + SPAM_C

average = total / count
print('Average spam confidence:', average)