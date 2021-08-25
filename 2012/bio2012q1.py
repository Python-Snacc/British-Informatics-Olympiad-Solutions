from collections import defaultdict

def solve():
    n = int(input())
    ans = 1
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            while not n%i:
                n //= i
            ans *= i
            if not n:
                return ans
    if ans == 1: # Prime
        return n
    return ans

def c(n):
    ans = 1
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            while not n % i:
                n //= i
            ans *= i
            if not n:
                return ans
    if ans == 1:  # Prime
        return n
    return ans

if __name__ == "__main__":
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    print(solve())
    # print("10, 20, 40, 50, 80, 100, 160, 200, 250, 320")
    seen = defaultdict(int)
    for i in range(1,1000001):
        if not i%10000:
            print(i)
        seen[c(i)] += 1
    occurences = 0
    largest = 0
    for x in seen:
        if seen[x] > occurences:
            largest = x
            occurences = seen[x]
    print(largest)