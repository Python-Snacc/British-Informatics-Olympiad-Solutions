from functools import lru_cache

@lru_cache(maxsize=None)
def num_arrangements(n):
    if n > 9:
        t = 0
        for i in range(n-9,n):
            t += num_arrangements(i)
        return t
    else:
        return 2**(n-1) if n else 1

answers = []
def solve():
    n, query = (int(x) for x in input().split())

    ans = []
    while True:
        if n == 0:
            break
        for i in range(1, min(10, n+1)):
            c = num_arrangements(n-i)
            if c >= query: # Right prefix
                ans.append(str(i))
                n -= i
                break
            else:
                query -= c
    print(" ".join(ans))

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
solve()