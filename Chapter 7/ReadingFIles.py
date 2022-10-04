fname = input('Enter FIle Name: ')
try:
    fhand = open(fname)
except:
    print('File not here', fname)
    quit()

count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count = count + 1
print('There are', count)