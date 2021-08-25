# Uses memoization for speed.
# Did you know that you can't memoize using a list as a key? My solution here was to use * to "unzip" it".

from functools import lru_cache
import time

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
l, p = input().split()
l = int(l)
wanted = l


@lru_cache(maxsize=None)
def valid(_tuple):
    if _tuple[0] < _tuple[1] and _tuple[2] < _tuple[1]:
        return True
    if _tuple[0] > _tuple[1]:
        return True
    return False


def valid2(_set):
    smallest = _set[0]
    for i in range(1, len(_set)):
        if _set[i] < smallest:
            smallest = _set[i]
        else:
            for j in range(i+1,len(_set)):
                if _set[j] > _set[i]:
                    return False
    return True

memo = {}

def count(length, letters, smallest, afterSmallest):
    if length==wanted:
        return 1
    total = 0
    for letter in letters:
        
        _smallest = smallest
        _afterSmallest = afterSmallest
        if letter < smallest:
            _smallest = letter
        elif afterSmallest == None:
            _afterSmallest = letter
        elif letter < afterSmallest:
            _afterSmallest = letter
        else:
            continue
        
        if length==1:
            temp = letters.copy()
            temp.remove(letter)
            if (length + 1, *temp, _smallest, _afterSmallest) in memo:
                total += memo[(length + 1, *temp, _smallest, _afterSmallest)]
            else:
                x = count(length + 1, temp, _smallest, _afterSmallest)
                memo[(length + 1, *temp, _smallest, _afterSmallest)] = x
                total += x
            continue
        # elif valid((string[-2],string[-1],letter)):
        temp = letters.copy()
        temp.remove(letter)
        #if valid2(string + [letter]):
        if (length + 1, *temp, _smallest, _afterSmallest) in memo:
            total += memo[(length + 1, *temp, _smallest, _afterSmallest)]
        else:
            x = count(length + 1, temp, _smallest, _afterSmallest)
            memo[(length + 1, *temp, _smallest, _afterSmallest)] = x
            total += x
    return total

letters = set(x for x in range(l))
used = list(ord(x)-ord("A") for x in p)

smallest = min(used)
y = used.index(smallest)
afterSmallest = None
if y != len(used) -1:
    afterSmallest = 50
    for a in range(y,len(used)):
        if used[a] < afterSmallest:
            afterSmallest = used[a]

for x in used:
    letters.remove(x)
if len(used) > 2:
    if valid2(used):
        start = time.time()
        print(count(len(used), letters, smallest, afterSmallest))
        print(time.time()-start)
    else:
        print(0)
else:
    start = time.time()
    print(count(len(used), letters, smallest, afterSmallest))
    print(time.time()-start)