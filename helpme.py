from pickle import APPEND


n = int(input())
i = 0
l = []

while i < n:
    i = i + 1
    l.append(i)

m = list(map(str, l))

n = ''.join(m)

print(n)
