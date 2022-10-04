#open file and read it line by line
#split line into a list of words using split()
#build a list of each words, check to see if word
#has been listed already or not
#sort the words then print

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(words)