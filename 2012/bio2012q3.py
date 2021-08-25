from collections import deque
# import time

digit_words = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX",
               7: "SEVEN", 8: "EIGHT", 9: "NINE", 0: "ZERO"}
words = {"ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ZERO"}
letters = ["O", "N", "E", "T", "W", "H", "R", "F", "U", "I", "V", "S", "X", "G", "Z"]

def number_to_word(n):
    if n==-1:
        return [""]
    t = []
    while n:
        t.append(digit_words[n % 10])
        n //= 10
    return t

def solve():
    answers = []
    for _ in range(3):
        s, f = (int(x) for x in input().split())
        # start = time.time()
        ts, tf = str(s), str(f)
        tts = ts
        for digit in tts:
            if digit in tf and digit in ts:
                tf = tf.replace(digit, "")
                ts = ts.replace(digit, "")
        s, f = int(ts) if ts else -1, int(tf) if tf else -1
        a, b = number_to_word(s), number_to_word(f)
        print(bfs("".join(a[::-1]), "".join(b[::-1])))
        # print(time.time()-start)

def count(start): # Returns tuple state
    return tuple((start.count("O"), start.count("N"),
           start.count("E"), start.count("T"),
           start.count("W"), start.count("H"),
           start.count("R"), start.count("F"),
           start.count("U"), start.count("I"),
           start.count("V"), start.count("S"),
           start.count("X"), start.count("G"),
           start.count("Z")))

numbers = [count("".join(number_to_word(i)[::-1])) for i in range(1,1000)]

def find_all_states(state):
    states = []
    for i in range(999):
        if sum(abs(numbers[i][j]-state[j]) for j in range(15)) < 6:
            states.append(numbers[i])
    return states

def bfs(start, target):
    # Numbers are made of O, N, E, T, W, H, R, F, U, I, V, S, X, G, Z
    start_state = count(start)
    end_state = count(target)
    seen = set()
    queue = deque()
    queue.append([start_state,0])
    while queue:
        cur = queue.popleft()
        if cur[0] in seen:
            continue
        seen.add(cur[0])
        new_states = find_all_states(cur[0])
        for i in range(len(new_states)):
            if new_states[i]==end_state:
                return cur[1]+1
            else:
                if new_states[i] not in seen:
                    queue.append([new_states[i], cur[1]+1])
                    # print(new_states[i])


if __name__ == "__main__":
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    solve()