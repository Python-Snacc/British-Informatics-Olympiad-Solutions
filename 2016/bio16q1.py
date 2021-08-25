def fraction(promenade):
    l, m = 1, 0
    r, s = 0, 1

    for i in range(len(promenade)):
        if promenade[i]=="L":
            l, m = l+r, s+m
        else:
            r, s = l+r, s+m

    print(f"{l+r}/{m+s}")

def _1b(): # LRL + LLLL = 4/5
    print("LRRR")

def _1c():
    print("999,999 Ls and 0 Rs")

def _1d():
    print("""No none do. The promenade before any choices has l,r,m,s equal to 1,0,0,1 respectively.
    When the next decision is an 'L', l=l+r and m=s+m; when it is 'R', r=l+r, s=s+m.
    Since both of these choices only add positive (including 0) integers together (since l,r,m,s are originally positive):
    l,r,m,s are always positive for any promenade. So every promenade of form (l+r)/(m+s) is positive.""")

if __name__=='__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    promenade = input()
    fraction(promenade)