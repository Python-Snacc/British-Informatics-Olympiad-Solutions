NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")

a, b, n = input().split()
n = int(n)

if n == 1:
    print(a)
    exit(0)
if n == 2:
    print(b)
    exit(0)

t = ord("A")-1
x, y = ord(a)-t, ord(b)-t

seen = {}
for i in range(2,n):
    x, y = y, x+y
    if y>26:
        y -= 26
    """
    if (x,y) in seen:
        print(i)
        print(seen[(x,y)])
        break
    else:
        seen[(x,y)]=i
    """


print(chr(y+t))
# print(chr(t+ord("X")-ord("F")))
## R
# print(chr(t+26+ord("H")-ord("Q")))
## Q

# print(10**15 % 84)
## 74
# C C 75 = K