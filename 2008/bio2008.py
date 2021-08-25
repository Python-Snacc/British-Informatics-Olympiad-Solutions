from collections import deque

def move1(_string):
    temp = _string[1:4]
    _string = temp + _string[0] + _string[4:]
    return _string

def move2(_string):
    temp = _string[3:6]
    _string = _string[:3] + _string[6] + temp
    return _string

def move3(_string):
    temp = _string[:3]
    _string = _string[3] + temp + _string[4:]
    return _string

def move4(_string):
    temp = _string[4:]
    _string = _string[:3] + temp + _string[3]
    return _string

def bfs():
    wanted = "1234567"
    seen = set()
    queue = deque()
    n = input()
    if n == wanted: return 0
    queue.append([n, 0])
    seen.add(n)
    while queue:
        cur, moves_taken = queue.popleft()
        new = move1(cur)
        if new not in seen:
            if new == wanted:
                return moves_taken + 1
            queue.append([new, moves_taken + 1])
            seen.add(new)

        new = move2(cur)
        if new not in seen:
            if new == wanted:
                return moves_taken + 1
            queue.append([new, moves_taken + 1])
            seen.add(new)

        new = move3(cur)
        if new not in seen:
            if new == wanted:
                return moves_taken + 1
            queue.append([new, moves_taken + 1])
            seen.add(new)

        new = move4(cur)
        if new not in seen:
            if new == wanted:
                return moves_taken + 1
            queue.append([new, moves_taken + 1])
            seen.add(new)


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
print(bfs())