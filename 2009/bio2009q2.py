from collections import deque

blocks = [[],[],[],[]] # Each sublist is a column
for _ in range(4):
    row = input()
    for i in range(4):
        blocks[i].append(row[i])

original = [i.copy() for i in blocks]

pos = [3, 3, 3, 3]

def remove_blocks(id_list): # [x1, y1], ...]
    id_list.sort(key=lambda p: p[1], reverse=True)
    for id in id_list:
        if len(blocks[id[0]])==1:
            blocks[id[0]] = []
        else:
            del blocks[id[0]][id[1]]

def fill_column(column_id):
    blocks[column_id].reverse()
    for i in range(len(blocks[column_id]), 4):
        blocks[column_id].append(original[column_id][pos[column_id]])
        pos[column_id] -= 1
        if pos[column_id] < 0:
            pos[column_id]=3
    blocks[column_id].reverse()

def bfs():
    global ans
    total = 1
    seen = set()
    points = 0
    to_be_deleted = []
    for i in range(4):
        for j in range(4):
            if (i,j) not in seen:
                cur = blocks[i][j]
                queue = deque()
                queue.append((i,j))
                points = 0
                temp = [(i,j)]
                while queue:
                    xy = queue.popleft()
                    points += 1
                    seen.add(xy)
                    if xy[0] < 3:
                        if (xy[0]+1, xy[1]) not in seen:
                            if blocks[xy[0]+1][xy[1]] == cur:
                                queue.append((xy[0]+1, xy[1]))
                                temp.append((xy[0]+1, xy[1]))
                                seen.add((xy[0]+1, xy[1]))
                    if xy[1] < 3:
                        if (xy[0], xy[1]+1) not in seen:
                            if blocks[xy[0]][xy[1]+1] == cur:
                                queue.append((xy[0], xy[1]+1))
                                temp.append((xy[0], xy[1]+1))
                                seen.add((xy[0], xy[1]+1))

                    if xy[0]:
                        if (xy[0]-1, xy[1]) not in seen:
                            if blocks[xy[0] - 1][xy[1]] == cur:
                                queue.append((xy[0]-1, xy[1]))
                                temp.append((xy[0]-1, xy[1]))
                                seen.add((xy[0]-1, xy[1]))
                    if xy[1]:
                        if (xy[0], xy[1]-1) not in seen:
                            if blocks[xy[0]][xy[1]-1] == cur:
                                queue.append((xy[0], xy[1]-1))
                                temp.append((xy[0], xy[1]-1))
                                seen.add((xy[0], xy[1]-1))

                if points > 1:
                    total *= points
                    to_be_deleted.extend(temp)
    if not to_be_deleted:
        print(ans)
        print("GAME OVER")
        exit(0)
    remove_blocks(to_be_deleted)
    for i in range(4):
        fill_column(i)
    return total if total > 1 else 0


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
ans = 0

while True:
    N = int(input())
    if N == 0:
        exit(0)
    for _ in range(N):
        ans += bfs()
    print("\n".join("".join(blocks[j][i] for j in range(4)) for i in range(4)))
    print(ans)