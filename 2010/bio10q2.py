class Grid():
    def __init__(self, row1, row2, row3):
        self.grid = [[1 for _ in range(11)] for _ in range(11)]
        self.grid[4][4:7]=row1
        self.grid[5][4:7]=row2
        self.grid[6][4:7]=row3

    def change_value(self, number, y, x):
        self.grid[y][x]+=number
        self.grid[y][x]-=1
        self.grid[y][x]%=6
        self.grid[y][x]+=1


class Dice():
    def __init__(self, grid): # Default values
        self.faces = {1: "top", 6: "bottom", 3: "left", 4: "right", 5: "front", 2: "back"}
        self.values = {"top": 1, "bottom": 6, "left": 3, "right": 4, "front": 5, "back": 2}
        self.pos = (5,5)
        self.grid = grid
        self.heading = "back"
        self.directions = {"front": (1,0), "right": (0,1), "back": (-1,0), "left": (0,-1)}

    def change_face(self, direction1, direction2):
        v1 = self.values[direction1]
        self.faces[v1]=direction2

    def update_values(self):
        for i in self.faces:
            self.values[self.faces[i]]=i

    def rotate(self, direction):
        if direction=="left":
            # Left becomes bottom, right becomes top, bottom becomes right, top becomes left
            self.change_face("left", "bottom")
            self.change_face("right", "top")
            self.change_face("bottom", "right")
            self.change_face("top", "left")
        elif direction=="right":
            self.change_face("right", "bottom")
            self.change_face("left", "top")
            self.change_face("bottom", "left")
            self.change_face("top", "right")
        elif direction=="front":
            self.change_face("front", "bottom")
            self.change_face("back", "top")
            self.change_face("bottom", "back")
            self.change_face("top", "front")
        elif direction=="back":
            self.change_face("back", "bottom")
            self.change_face("front", "top")
            self.change_face("bottom", "front")
            self.change_face("top", "back")

        self.update_values()

    def move(self):
        y, x = self.pos
        self.grid.change_value(self.values["top"], y, x)
        value = self.grid.grid[y][x]
        if value == 1 or value == 6: pass
        elif value == 3 or value == 4:
            self.heading = self.faces[7 - self.values[self.heading]]
        elif value == 2:
            if self.heading == "front":
                self.heading = "left"
            elif self.heading == "back":
                self.heading = "right"
            elif self.heading == "left":
                self.heading = "back"
            elif self.heading == "right":
                self.heading = "front"
        elif value == 5:
            if self.heading == "left":
                self.heading = "front"
            elif self.heading == "right":
                self.heading = "back"
            elif self.heading == "back":
                self.heading = "left"
            elif self.heading == "front":
                self.heading = "right"

        a, b = self.directions[self.heading]
        self.pos = ((self.pos[0] + a)%11, (self.pos[1] + b)%11)
        self.rotate(self.heading)

    def __str__(self):
        y = self.pos[0]
        x = self.pos[1]
        ans = []
        for j in range(y-1,y+2):
            temp = ""
            for i in range(x-1,x+2):
                if j>10 or i>10 or j<0 or i<0:
                    temp += "X"
                else:
                    temp += str(self.grid.grid[j][i])
            ans.append(temp)
        return "\n".join(ans)


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")

rows = [[int(x) for x in input().split()] for _ in range(3)]
grid = Grid(rows[0], rows[1], rows[2])
dice = Dice(grid)

while True:
    n = int(input())
    if n==0:
        break
    for _ in range(n):
        dice.move()
    print(dice)