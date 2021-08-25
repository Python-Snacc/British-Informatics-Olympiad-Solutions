string = input()
s, p = (int(x) for x in input().split())

def count(letter, steps):
    if letter == "A":
        a, b = 1, 0
        for i in range(steps):
            a, b = b, a + b
        return a + b

    if letter == "B":
        a, b = 0, 1
        for i in range(steps):
            a, b = b, a + b
        return a + b

    if letter == "C":
        return 2 ** steps

    if letter == "D":
        return 2 ** steps

    if letter == "E":
        return 2 ** steps

ans = ""

def change(word):
    new = ""
    for letter in word:
        if letter == "A":
            new += "B"
        elif letter == "B":
            new += "AB"
        elif letter == "C":
            new += "CD"
        elif letter == "D":
            new += "DC"
        elif letter == "E":
            new += "EE"
    return new

for j in range(s, 0, -1):
    t = p
    for i in range(len(string)):
        x = count(string[i], j)
        if x >= t:
            string = change(string[:i+1])
            break
        else:
            t -= x
temp = string[:p]
ans = f"{temp.count('A')} {temp.count('B')} {temp.count('C')} {temp.count('D')} {temp.count('E')}"
print(ans)