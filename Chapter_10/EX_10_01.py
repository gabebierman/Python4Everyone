from multiprocessing.sharedctypes import Value
from pickletools import read_stringnl_noescape_pair


fname = input('Enter File: ')
if len(fname) < 1 : fname = 'txt.txt'
hand = open(fname)

di = dict()

for lin in hand :
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds :
       #retrieve create update
       di[w] = di.get(w,0) + 1


#print(di)

tmp =list()
for k,v in di.items() :
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)

#print(tmp)


tmp = sorted(tmp, reverse=True)
print('Sorted', tmp[:5])


for v,k in tmp[:5] :
    print(k,v)