import time
from bisect import bisect_left, bisect_right

def lucky(lst, first):
    for j in range(len(lst)-1, -1, -1):
        if (j-1) and not (j+1)%first:
            del lst[j]
    return lst

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    n = int(input())
    start = time.time()
    odd = [2*i+1 for i in range(5200)]
    first_number = odd[1]
    index = 1
    while first_number < n and index<16:
        lucky(odd, first_number)
        index += 1
        first_number = odd[index]

    print(f"{odd[bisect_left(odd, n)-1]} {odd[bisect_right(odd, n)]}")

    print(time.time()-start)
