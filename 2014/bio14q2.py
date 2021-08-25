
redTiles = {1: [[1,1,3,4,5,6],[(-1,0),(1,0),(1,0),(1,0),(-1,0),(-1,0)]], 2: [[2,2,3,4,5,6],[(0,-1),(0,1),(0,1),(0,-1),(0,-1),(0,1)]],
            3: [[1,2,4,5,5,6],[(-1,0),(0,-1),(0,-1),(-1,0),(0,-1),(-1,0)]], 4: [[1,2,3,5,6,6],[(-1,0),(0,1),(0,1),(-1,0),(0,1),(-1,0)]],
            5: [[1,2,3,3,4,6],[(1,0),(0,-1),(1,0),(0,1),(1,0),(0,1)]], 6: [[1,2,3,4,4,5],[(1,0),(0,-1),(1,0),(1,0),(0,-1),(0,-1)]]}

greenTiles = {2: [[2,2,5,6,3,4],[(-1,0),(1,0),(1,0),(1,0),(-1,0),(-1,0)]], 1: [[1,1,5,6,3,4],[(0,-1),(0,1),(0,1),(0,-1),(0,-1),(0,1)]],
            5: [[2,1,6,3,3,4],[(-1,0),(0,-1),(0,-1),(-1,0),(0,-1),(-1,0)]], 6: [[2,1,5,3,4,4],[(-1,0),(0,1),(0,1),(-1,0),(0,1),(-1,0)]],
            3: [[2,1,5,5,6,4],[(1,0),(0,-1),(1,0),(0,1),(1,0),(0,1)]], 4: [[2,1,5,6,6,3],[(1,0),(0,-1),(1,0),(1,0),(0,-1),(0,-1)]]}

r_total = 0
g_total = 0
found = False


def RedConnect(pos, start, used, points=0):
    currentUsed = used.copy()
    global r_total, found
    if pos==start and points>3:
        r_total += points/sum(1 for i in used if grid[i[0]][i[1]]==5 )
        found = True
        return
    row, column = pos[0], pos[1]
    directions = redTiles[grid[row][column]][1]
    wantedTiles = redTiles[grid[row][column]][0]
    connections = 0
    for k in range(len(directions)):
        up, right = directions[k]
        used = currentUsed.copy()
        try:
            if grid[row + up][column + right] == wantedTiles[k] and row +up >=0 and column + right >=0:
                connections += 1
                newTile = [row + up,column + right]
                if newTile not in used or (newTile==start and points > 2):
                    if newTile not in used:
                        used.append([row, column])
                    RedConnect(newTile, start,used,points + 1)
                    if found:
                        break
        except IndexError:
            pass

def GreenConnect(pos, start, used, points=0):
    currentUsed = used.copy()
    global g_total, found
    if pos==start and points>3:
        g_total += points/sum(1 for i in used if grid[i[0]][i[1]]==3 )
        found = True
        return
    row, column = pos[0], pos[1]
    directions = greenTiles[grid[row][column]][1]
    wantedTiles = greenTiles[grid[row][column]][0]
    connections = 0
    for k in range(len(directions)):
        up, right = directions[k]
        used = currentUsed.copy()
        try:
            if grid[row + up][column + right] == wantedTiles[k] and row +up >=0 and column + right >=0:
                connections += 1
                newTile = [row + up,column + right]
                if newTile not in used or (newTile==start and points > 2):
                    if newTile not in used:
                        used.append([row, column])
                    GreenConnect(newTile, start,used,points + 1)
                    if found:
                        break
        except IndexError:
            pass


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

# Red Player
for row in range(n-1):
    for column in range(n-1):
        if grid[row][column] != 5:
            continue
        found = False
        RedConnect([row, column], [row, column],[])


# Green Player
for row in range(n-1):
    for column in range(n-1):
        if grid[row][column] != 3:
            continue
        found = False
        GreenConnect([row, column], [row, column],[])

print(f"{int(r_total)} {int(g_total)}")
