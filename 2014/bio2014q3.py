import math
from functools import lru_cache
@lru_cache(maxsize=None)
def comb(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
n = int(input())

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def build(n, targetLen, ans=""):
    if targetLen == 0:
        return ans
    start = (alpha.index(ans[-1]) + 1) if ans else 0
    for letter in range(start, 36):

        can = comb(36 - (letter + 1), targetLen - 1)
        print(can)

        if can >= n:
            return build(n, targetLen - 1, ans + alpha[letter]) # Right prefix
        n -= can


targLen = 1
while comb(36, targLen) < n:
    n -= comb(36, targLen)
    targLen += 1
print(n)

print(build(n, targLen))