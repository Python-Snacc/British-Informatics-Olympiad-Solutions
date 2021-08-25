from collections import deque

grid = [[0 for _ in range(5)] for _ in range(5)]

def solve():
    pos_list = convert_to_num(input())
    for y,x, n in pos_list:
        grid[y][x] += n
    print(bfs(convert_to_string(grid)))


def convert_to_num(string):
    lst = []
    for letter in string:
        if letter.isupper():
            ans = ord(letter) - ord("A")
            lst.append([ans // 5, ans % 5, 2])
        else:
            ans = ord(letter) - ord("a")
            lst.append([ans // 5, ans % 5, 1])
    return lst

def convert_to_string(array):
    ans = ""
    for i in range(5):
        for j in range(5):
            if not array[i][j]:
                continue
            if array[i][j]==1:
                ans += chr(i*5+j + ord("a"))
            else:
                ans += chr(i*5+j + ord("A"))
    return ans

def light(array, position, presses):
    y, x = position // 5, position % 5
    array[y][x] = (array[y][x] + presses) % 3
    if y: array[y-1][x] = (array[y-1][x] + presses) % 3
    if x: array[y][x-1] = (array[y][x-1] + presses) % 3
    if y != 4: array[y+1][x] = (array[y+1][x] + presses) % 3
    if x != 4: array[y][x+1] = (array[y][x+1] + presses) % 3

def bfs(string):
    start = string
    prev = {string: ""}
    prev_action = {string: ""}
    queue = deque()
    queue.append(string)
    while queue:
        cur = queue.popleft()
        for i in range(25):
            for j in range(1,3):
                x = [[0 for _ in range(5)] for _ in range(5)]
                pos_list = convert_to_num(cur)
                for y, z, n in pos_list:
                    x[y][z] += n
                light(x, i, j)
                new = convert_to_string(x)
                if new not in prev:
                    if new == "":
                        actions = chr(i + ord("a")) if j==1 else chr(i + ord("A"))
                        while cur != start:
                            pos, presses = prev_action[cur]
                            if presses==1:
                                actions += chr(pos + ord("a"))
                            else:
                                actions += chr(pos + ord("A"))
                            cur = prev[cur]
                        return actions[::-1]
                    else:
                        prev[new] = cur
                        prev_action[new] = (i, j)
                        queue.append(new)
    return "IMPOSSIBLE"

if __name__ == "__main__":
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    solve()