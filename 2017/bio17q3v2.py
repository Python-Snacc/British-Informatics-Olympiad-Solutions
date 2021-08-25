from itertools import product
from collections import defaultdict
import time

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
p,i,n,w = (int(x) for x in input().split())

start = time.time()
"""
weights = [x for x in range(1,i+1)]

for a in range(1,n-p+2):
    for x in product(weights, repeat= a):
        if sum(x) == w:
            combs.add(tuple(sorted(x)))
print(combs)


distribution = 0

for x in product(combs, repeat=p):
    if sum(len(y) for y in x) == n:
        distribution += 1

print(distribution)
"""


def findNum(remainingNum, currentSet=[[]], maximum=100000, wantedLength = 0):
    x = []
    #print((remainingNum,currentSet))
    if remainingNum == 0:
        if wantedLength:
            if len(currentSet[0]) != wantedLength:
                return None
        return currentSet
    if wantedLength:
        if len(currentSet) > wantedLength:
            return 
    for i in range(1,min(maximum + 1,remainingNum + 1)):
        y = []
        for a in currentSet:
            y.append(a + [i])
        z = findNum(remainingNum-i, y, maximum, wantedLength)
        if wantedLength and z is None:
            continue
        else:
            x += z
            
        
        #print(x)

    return x

temp = findNum(w, [[]], i)

combs = []
for x in temp:
    if sorted(x) not in combs:
        combs.append(x)

distribution = findNum(n, wantedLength = p)

print(time.time()-start)

lengths = defaultdict(int)
for x in combs:
    lengths[len(x)] += 1

total = 0
for x in distribution:
    c = 1
    for y in x:
        c *= lengths[y]
    total += c

print(total)
print(time.time()-start)
#for i in range(p)

