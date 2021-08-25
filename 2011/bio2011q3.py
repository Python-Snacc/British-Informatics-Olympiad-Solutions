from bisect import bisect_left

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
n = int(input())
import time
start = time.time()

upside_down_numbers = [5, 19, 28, 37, 46, 55, 64, 73, 82, 91]
if n<=10:
    print(upside_down_numbers[n-1])
    exit(0)

n -= 10
min = 10
while True:
    new = []
    pos = bisect_left(upside_down_numbers, min)
    min *= 10
    new = []
    k = 9 * pos
    for j in range(1,10):
        for i in range(pos):
            new.append(j*min + upside_down_numbers[i]*10 + 10-j)
            n -= 1
            if n==0:
                print(new[-1])
                print(time.time()-start)
                exit(0)
    upside_down_numbers = [upside_down_numbers[i] for i in range(pos, len(upside_down_numbers))] + new