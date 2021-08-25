morse_code = {"a": ".-",  "h": "....", "o":	"---", "v": "...-", "b": "-...", "i": "..",	"p": ".--.",
              "w": ".--", "c": "-.-.", "j": ".---", "q": "--.-", "x": "-..-", "d": "-..", "k": "-.-",
              "r": ".-.", "y": "-.--", "e": ".", "l": ".-..", "s": "...", "z": "--..", "f": "..-.",
              "m": "--", "t": "-", "g":	"--.", "n":	"-.", "u": "..-"}
ans = 0


def find_words(morse, extra_letters, original_length):
    global ans
    if original_length == 0:
        return
    for letter in morse_code:
        c = len(morse_code[letter])
        if c > extra_letters:
            continue
        if morse_code[letter] == morse[:c]:
            if c == extra_letters:
                if original_length == 1:
                    ans += 1
            else:
                find_words(morse[c:], extra_letters-c, original_length-1)


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
word = input()
m = "".join(morse_code[letter] for letter in word)
find_words(m, len(m), len(word))

print(ans)
