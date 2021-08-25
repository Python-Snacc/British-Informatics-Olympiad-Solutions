from functools import lru_cache
from collections import defaultdict
import time


@lru_cache(maxsize=None)
def mid(middle, left, right):
    return middle < max(left, right) and middle > min(left,right)


connections = defaultdict(set)
seen = set()


@lru_cache(maxsize=None)
def createEquivalences(string):
    seen.add(string)
    if len(string) < 3:
        connections[string] = set()

    for i in range(len(string)-1):
        if i:
            if mid(string[i-1], string[i], string[i+1]):
                connections[string].add(string[:i]+string[i+1] + string[i] + string[i+2:])
                continue
        if i!=len(string)-2:
            if mid(string[i+2], string[i], string[i+1]):
                connections[string].add(string[:i]+string[i+1] + string[i] + string[i+2:])
                continue
    for x in connections[string]:
        if x not in seen:
            createEquivalences(x)


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
input()
string = input()
start = time.time()
createEquivalences(string)


def bfs(source):
    seen = set()
    queue = []
    depths = defaultdict(int)
    queue.append((source,0))
    seen.add(source)
    
    while queue:
        x, depth = queue.pop(0)
        depths[x] = depth

        for c in connections[x]:
            if c not in seen:
                queue.append((c,depth+1))
                seen.add(x)

    return depths
            

print(max(bfs(string).values()))
print(time.time()-start)
