class Grid():

    def __init__(self, trail_memory):
        self.memory = trail_memory
        self.trail = []

    def update_grid(self, former_position):
        self.trail.append(former_position)
        if len(self.trail) > self.memory:
            del self.trail[0]
    
    def valid_move(self, new_position):
        if new_position in self.trail:
            return False
        else:
            return True

class Agent():

    def __init__(self, t, instructions, moves):
        self.instructions = instructions * (moves//len(instructions)) + instructions[:moves%len(instructions)]
        self.directionList = ["F", "R", "B", "L"]
        self.direction = 0
        self.position = (0,0)
        self.grid = Grid(t)
        self.realDirectionDict = [(0,1), (1,0), (0,-1), (-1,0)]

    def explore(self):
        for instruction in self.instructions:
            moveable = 4
            while True:
                if moveable == 0:
                    break
                new_direction = self.direction + self.directionList.index(instruction)
                new_direction %= 4
                new_position = self.change(self.position, self.realDirectionDict[new_direction])
                if self.grid.valid_move(new_position):
                    self.grid.update_grid(self.position)
                    self.position = new_position
                    self.direction = new_direction
                    break
                else:
                    self.direction += 1
                    self.direction %= 4
                    moveable -= 1
        print(self.position)

    def change(self, pos, move):
        return (pos[0] + move[0], pos[1] + move[1])

    def c(self):
        pos = []
        for x in range(-10,11):
            for y in range(-10,11):
                pos.append((x,y))

        ans = 0
        
        while True:
            if self.position in pos:
                pos.remove(self.position)
                if len(pos) == 0:
                    break
            
            ans += 1
            moveable = 4
            while True:
                if moveable == 0:
                    break
                new_direction = self.direction + self.directionList.index("L")
                new_direction %= 4
                new_position = self.change(self.position, self.realDirectionDict[new_direction])
                if self.grid.valid_move(new_position):
                    self.grid.update_grid(self.position)
                    self.position = new_position
                    self.direction = new_direction
                    break
                else:
                    self.direction += 1
                    self.direction %= 4
                    moveable -= 1
        print(ans)

    def d(self):
        for i in range(100):
            for instruction in self.instructions:
                moveable = 4
                while True:
                    if moveable == 0:
                        return False
                    new_direction = self.direction + self.directionList.index(instruction)
                    new_direction %= 4
                    new_position = self.change(self.position, self.realDirectionDict[new_direction])
                    if self.grid.valid_move(new_position):
                        self.grid.update_grid(self.position)
                        self.position = new_position
                        self.direction = new_direction
                        break
                    else:
                        self.direction += 1
                        self.direction %= 4
                        moveable -= 1

        return True
        
    
def c():
    agent = Agent(1000000, "L", 1)
    agent.c()
    # Result 440

def d():
    t = 1300
    while True:
        agent = Agent(t, "LLRFFF", 6)
        if agent.d():
            t -= 1
        elif t < 100:
            print("Fail")
            break
        else:
            print(t)
            break

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        print("\n")
        t, i, m = input().split()
        t, m = int(t), int(m)
        agent = Agent(t, i, m)
        agent.explore()

    
