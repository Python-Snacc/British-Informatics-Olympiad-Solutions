# 30 / 32

"""
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a, b, c, d, n = (int(x) for x in input().split())
Sum = a+b+c+d
temp = [a,b,c,d]

total = factorial(Sum)/factorial(a)/factorial(b)/factorial(c)/factorial(d)

ans = ""

while any(temp):
    c = total/sum(temp)
    pos = n/c
    
    k = 0
    for i in range(len(temp)):
        if temp[i]==0:
            k += 1
        if pos>temp[i]:
            pos -= temp[i]
        else:
            break
    ans += "ABCD"[i]
    
    n -= c*sum(temp[:i])
    temp[i] -= 1
    total = factorial(sum(temp))
    for k in temp:
        total /= factorial(k)

print(ans)
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def total_ways(a, b, c, d): 
    return factorial(a+b+c+d)//(factorial(a)*factorial(b)*factorial(c)*factorial(d)) 

def g(a, b, c, d, n): 
    if a==0 and b==0 and c==0 and d==0: 
        return '' 
    ways=total_ways(a, b, c, d) 

    if n <= (ways*a)//(a+b+c+d) and a>0: ##letter is 'A' 
        return 'A'+g(a-1, b, c, d, n) 

    if n <= (ways*(a+b))//(a+b+c+d) and b>0: ##letter is 'B' 
        return 'B'+g(a, b-1, c, d, n-(ways*a)//(a+b+c+d)) 

    if n <= (ways*(a+b+c))//(a+b+c+d) and c>0: ##letter is 'C' 
        return 'C'+g(a, b, c-1, d, n-(ways*(a+b))//(a+b+c+d))

    else: ##letter is 'D' 
        return 'D'+g(a, b, c, d-1, n-(ways*(a+b+c))//(a+b+c+d)) 

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
a, b, c, d, n = (int(x) for x in input().split()) 

print(g(a, b, c, d, n))
