from string import ascii_uppercase

def occurences(word):
    return tuple(word.count(letter) for letter in ascii_uppercase)

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
w1 = input()
w2 = input()

if occurences(w1) == occurences(w2):
    print("Anagrams")
else:
    print("Not anagrams")