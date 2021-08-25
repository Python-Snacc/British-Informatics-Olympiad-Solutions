from collections import defaultdict
NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
n=int(input())
anagram = defaultdict(int)
k = n
while k!=0:
    anagram[k%10] += 1
    k//=10
ans = []
for i in range(2,10):
    original = anagram.copy()
    new = n*i
    ok = True
    while new!=0:
        if not original[new%10]:
            ok = False
            break
        original[new%10] -= 1
        new//=10
    if ok:
        ans.append(str(i))
print(" ".join(ans) if ans else "NO")
"""
c = 85247910
anagram2 = defaultdict(int)
while c!=0:
    anagram2[c%10] += 1
    c//=10
c = 85247910
for i in range(2,10):
    if not c%i:
        original = anagram2.copy()
        new = c//i
        if len(str(new)) != len(str(c)):
            continue
        ok = True
        while new!=0:
            if not original[new%10]:
                ok = False
                break
            original[new%10] -= 1
            new//=10
        if ok:
            print(c//i)
"""