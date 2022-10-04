name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

hand = open(name)
di =dict()



for lin in hand :
    if not lin.startswith('From ') :
        continue
    lin = lin.rstrip()
    wds = lin.split()
    colpos = wds[5].find(':')
    hour = wds[5][:colpos]

    di[hour] = di.get(hour,0) + 1



#read the colon position, create variable point 
# and then colpos-1


tmp =list()
for k,v in di.items() :
    #print(k,v)
    newt = (k,v)
    tmp.append(newt)

#print(tmp)


tmp = sorted(tmp)
#print('Sorted', tmp[:5])


for v,k in tmp :
    print(v,k)