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
    di[wds[1]] = di.get(wds[1],0) + 1

    #print(w)
    #print(wds)


largest = -1 
theword = None
for k,v in di.items() :
    #print(k,v)
    if v > largest : 
        largest  = v
        theword = k

print(theword , largest)

