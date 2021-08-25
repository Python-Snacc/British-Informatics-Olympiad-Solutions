def solve(word):
    n = len(word)
    possible = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for digit in possible:
        pos = 0
        c = len(digit)
        for i in range(n):
            if word[i]==digit[pos]:
                pos += 1
            if pos==c:
                print(possible.index(digit) + 1)
                exit(0)
    print("NO")

if __name__=="__main__":
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    word = input()
    solve(word)
