from functools import lru_cache
NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
s, d = (int(x) for x in input().split())

@lru_cache(maxsize=None)
def make_num(target, throws_left, throws_so_far=0, points=0):
    if points == target:
        if throws_left == 0:
            return 1
    elif points > target:
        return 0
    elif throws_left == 0:
        return 0

    total = 0
    if throws_so_far == 0:
        for i in range(1,21):
             total += make_num(target, throws_left - 1, throws_so_far + 1, points + i*2)
    else:
        for i in range(1,21):
             total += make_num(target, throws_left - 1, throws_so_far + 1, points + i)
    return total

print(make_num(s, d))