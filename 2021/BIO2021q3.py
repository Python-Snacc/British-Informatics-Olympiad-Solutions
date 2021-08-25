from collections import deque
from itertools import permutations
warehouse = ["A", "B", "C", "D", "E", "F", "G", "H"]


# Implement the three operations in the question.
def add(cur):
    cur += warehouse[len(cur)]
    return cur


def swap(cur):
    return cur[:2][::-1] + cur[2:]


def rotate(cur):
    return cur[1:] + cur[0]


def bfs(start, target):
    steps = {start: 0}  # Stores number of steps required to get to a state.
    queue = deque()
    queue.append(start)
    target_len = len(target)
    cur = ""
    res = None

    def on_reached(state):
        # We only care if the new value hasn't been reached.
        # If it has been reached earlier, it was reached in the same or fewer steps.
        if state not in steps:
            steps[state] = steps[cur] + 1
            if state == target:
                return steps[state]
            queue.append(state)

    while queue:
        cur = queue.popleft()
        len_cur = len(cur)

        if len_cur < target_len:  # If there are boxes left at the warehouse
            new = add(cur)
            # Call the on_reached() function and return the result if it exists.
            res = on_reached(new)
            if res:
                return res

        if len_cur > 1:  # If at least two boxes
            new = swap(cur)
            res = on_reached(new)
            if res:
                return res

        if len_cur:  # If at least one box
            new = rotate(cur)
            res = on_reached(new)
            if res:
                return res


def solve():
    global warehouse
    target = input()
    start = ""
    warehouse = warehouse[:len(target)]
    print(bfs(start, target))  # Find the minimum steps to get from the start state to the target state.


def b():
    global warehouse
    p = ["".join(s) for s in permutations("ABCDE")]
    warehouse = warehouse[:5]

    for string in p:
        min_ops = bfs("", string)
        if min_ops == 6:
            print(string)


def modified_bfs(start, target, length):
    # Instead of storing the minimum steps to reach a state,
    # let's store the ways to make a state in a certain number of steps.
    # e.g. we can make the starting value in 0 steps in exactly 1 way!
    ways = {(start, 0): 1}
    queue = deque()
    queue.append((start, 0))
    target_len = len(target)

    while queue:
        cur, steps = queue.popleft()

        if steps == length:
            print(ways[(target, length)])  # 84
            exit(0)

        len_cur = len(cur)

        if len_cur < target_len:
            new = add(cur)
            if (new, steps+1) not in ways:
                ways[(new, steps+1)] = ways[(cur, steps)]
                queue.append((new, steps+1))

            else:
                ways[(new, steps+1)] += ways[(cur, steps)]

        if len_cur > 1:  # If at least two boxes
            new = swap(cur)
            if (new, steps + 1) not in ways:
                ways[(new, steps + 1)] = ways[(cur, steps)]
                queue.append((new, steps + 1))

            else:
                ways[(new, steps + 1)] += ways[(cur, steps)]

        if len_cur:  # If at least one box
            new = rotate(cur)
            if (new, steps + 1) not in ways:
                ways[(new, steps + 1)] = ways[(cur, steps)]
                queue.append((new, steps + 1))

            else:
                ways[(new, steps + 1)] += ways[(cur, steps)]


def c():
    modified_bfs("", "HGFEDCBA", 24)


if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    solve()
