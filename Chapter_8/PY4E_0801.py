han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('line:', line)
    if line == '' :
        #print('skip blank')
        continue
    wds = line.split()
   # print('Wrds: ',wds)
   #the following is guardian
    if len(wds) < 3 :
        continue
    if wds[0] != 'From' :
       # print('ignore')
        continue
    print(wds[2])