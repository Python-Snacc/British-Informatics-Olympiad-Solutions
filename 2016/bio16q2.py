from collections import defaultdict
squares = defaultdict(int)

def pos2d(pos1d):
    pos1d -= 1
    return (pos1d//5, pos1d%5)

def migrate(pos2d):
    squares[pos2d] -= 4
    y, x = pos2d
    squares[(y+1, x)] += 1
    while squares[(y+1, x)] > 3:
        migrate((y+1,x))
    squares[(y-1, x)] += 1
    while squares[(y-1, x)] > 3:
        migrate((y-1,x))
    squares[(y, x+1)] += 1
    while squares[(y, x+1)] > 3:
        migrate((y,x+1))
    squares[(y, x-1)] += 1
    while squares[(y, x-1)] > 3:
        migrate((y,x-1))

def step(pos1d):
    pos = pos2d(pos1d)
    squares[pos] += 1
    while squares[pos]>3:
        migrate(pos)

def _2b():
    print(7) # WRONG 16

def _2c():
    # 6,8,11,16, 18,21,1, 3
    print("6 3 8")
    print("2 3 5")
    starts = [1,3,6,8,11,16,18,21]
    total = 0
    for start in starts:
        for i in range(25):
            for j in range(25):
                if i==j:
                    continue
                for k in range(25):
                    seen = set()
                    if k==j or k==i:
                        continue
                    seen.add(start)
                    seen.add((start+i)%25)
                    seen.add((start+i+j)%25)
                    seen.add((start+i+j+k)%25)
                    seen.add((start+i*2+j+k)%25)
                    seen.add((start+i*2+j*2+k)%25)
                    seen.add((start+i*2+j*2+k*2)%25)
                    seen.add((start+i*3+j*2+k*2)%25)
                    for s in starts:
                        if s not in seen:
                            total -= 1
                            break
                    total += 1
    print(total)

def _2d():
    print("""No you cannot always determine the landscape. This is because of the possibility of multiple migrations.
    For example take the end landscape, given that the person was added to position 8:
    0 1 1 0 0
    1 0 1 1 0
    0 1 1 0 0
    0 0 0 0 0
    0 0 0 0 0
    The original landscape could have been either:
    0 0 0 0 0
    0 3 3 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    or 
    0 1 1 0 0
    1 0 0 1 0
    0 1 1 0 0
    0 0 0 0 0
    0 0 0 0 0""")

if __name__=='__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    p, s, n = (int(x) for x in input().split())
    seq = [int(x) for x in input().split()]
    done = False

    while not done:
        for pos in seq:
            step(p)
            p += pos
            p-=1
            p %= 25
            p+=1
            n -= 1
            if n==0:
                done=True
                break
    for i in range(5):
        to_print = []
        for j in range(5):
            to_print.append(str(squares[(i,j)]))
        print(" ".join(to_print))