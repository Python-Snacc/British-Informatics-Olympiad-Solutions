NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
a, c, m = (int(x) for x in input().split())
r = 0

class Grid():
    def __init__(self):
        self.grid = [[0 for _ in range(10)] for __ in range(10)]

    def place(self, x,y):
        self.grid[9-y][x] = 1

    def valid(self, x,y):
        try:
            if self.grid[9-y][x]:
               return False
        # If that square is not on the board, it isn't valid
        except IndexError:
            return False
        try:
            if self.grid[9-y][x-1]:
               return False
        except IndexError: pass
        try:
            if self.grid[9-y][x+1]:
               return False
        except IndexError: pass
        try:
            if self.grid[8-y][x-1]:
               return False
        except IndexError: pass
        try:
            if self.grid[8-y][x+1]:
               return False
        except IndexError: pass
        try:
            if self.grid[8-y][x]:
               return False
        except IndexError: pass
        try:
            if self.grid[10-y][x]:
               return False
        except IndexError: pass
        try:
            if self.grid[10-y][x+1]:
               return False
        except IndexError: pass
        try:
            if self.grid[10-y][x-1]:
               return False
        except IndexError: pass
        
        return True

toPlace = [4,3,3,2,2,2,1,1,1,1]
board = Grid()

for ship in toPlace:
    valid = False
    while True:
        r = (a*r+c)%m
        
        x = r%10
        y = (r%100)//10
        r = (a*r+c)%m
        d = r%2
        direction = "V" if d else "H"
        ty = y
        tx = x
        b = False
        for _ in range(ship):
            if board.valid(tx, ty):
                if d:
                    ty += 1
                else:
                    tx += 1
            else:
                b = True
                break
        if b:
            continue
        ty = y
        tx = x
        for _ in range(ship):
            board.place(tx,ty)
            if d:
                ty += 1
            else:
                tx += 1
                
        print(f"{x} {y} {direction}")
        break
