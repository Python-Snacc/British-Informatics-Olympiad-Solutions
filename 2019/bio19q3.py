# Uses LRU cache for speed

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

def to_tuple(set_obj):
    """Converts a set to an ordered tuple"""
    return tuple(sorted(list(set_obj)))

def remove(tuple_obj, obj):
    """Removes an item from a tuple"""
    list_obj = list(tuple_obj)
    list_obj.remove(obj)
    return tuple(list_obj)

@lru_cache(maxsize=None)
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
    
        temp = remove(letters, letter)
        x = count(length + 1, temp, _smallest, _afterSmallest)
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

letters = to_tuple(letters) # Convert to tuple for LRU caching

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