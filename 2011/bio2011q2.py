from collections import deque

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suits = ["C", "H", "S", "D"]
before_dealing = deque()
for s in suits:
    for i in values:
        before_dealing.append(i+s)

piles = []
abcdef = [int(x) for x in input().split()]

i = 0
seen = set()
while before_dealing:
    for _ in range(abcdef[i]-1):
        before_dealing.append(before_dealing.popleft())
    piles.append([1, before_dealing.popleft()])
    i += 1
    i %= 6

print(f"{piles[0][1]} {piles[-1][1]}")

original = [piles[i].copy() for i in range(len(piles))]
# print(original)

def move(index1, index2): # Move pile one onto pile 2
    piles[index2][0] += piles[index1][0]
    piles[index2][1] = piles[index1][1]
    del piles[index1]

def check_validity(index1, index2):
    if index2 < 0:
        return False
    if piles[index1][1][0] == piles[index2][1][0] or piles[index1][1][1] == piles[index2][1][1]:
        return True
    return False

game_continue = True
while game_continue:
    if len(piles)==1:
        break
    i = len(piles)-1
    while True:
        if i == 0: # No valid moves
            game_continue=False
            break

        # Check adjacent pile
        if check_validity(i, i-1):
            move(i, i-1)
            break

        # Check separated pile
        elif check_validity(i, i-3):
            move(i,i-3)
            break

        i -= 1

print(f"{len(piles)} {piles[0][1]}")

# print(piles)
piles = [original[i].copy() for i in range(len(original))]
# print(piles)

while True:
    if len(piles)==1:
        break
    largest = 0
    indices = []
    for i in range(len(piles)-1, 0, -1):
        if check_validity(i, i-1):
            c = largest
            largest = max(largest, piles[i][0] + piles[i-1][0])
            if c!=largest:
                indices = [i, i-1]
        if check_validity(i, i-3):
            c = largest
            largest = max(largest, piles[i][0] + piles[i-3][0])
            if c!=largest:
                indices = [i, i-3]
    if not indices:
        break
    move(indices[0], indices[1])

print(f"{len(piles)} {piles[0][1]}")

piles = [original[i].copy() for i in range(len(original))]
# piles = [[1, "AD"], [3, "8S"], [1, "8D"], [2, "4S"], [1, "TH"], [2, "KD"], [2, "4D"], [1, "TC"]]

def find_valid(index1, index2):
    temp = [piles[i].copy() for i in range(len(piles))]
    temp[index2][0] += temp[index1][0]
    temp[index2][1] = temp[index1][1]
    del temp[index1]

    moves = 0

    def valid(i1, i2):
        if i2 < 0:
            return False
        if temp[i1][1][0] == temp[i2][1][0] or temp[i1][1][1] == temp[i2][1][1]:
            return True
        return False

    for i in range(len(temp)-1, 0, -1):
        if valid(i, i-1):
            moves += 1
        if valid(i, i-3):
            moves += 1

    return moves

while True:
    if len(piles)==1:
        break
    largest = 0
    indices = []
    possible = False
    for i in range(len(piles)-1, 0, -1):
        if check_validity(i, i-1):
            possible = True
            c = largest
            largest = max(largest, find_valid(i, i-1))
            if c!=largest or largest==0:
                indices = [i, i-1]
        if check_validity(i, i-3):
            possible = True
            c = largest
            largest = max(largest, find_valid(i, i-3))
            if c!=largest or largest==0:
                indices = [i, i-3]
    if not indices and not possible:
        break
    move(indices[0], indices[1])

print(f"{len(piles)} {piles[0][1]}")