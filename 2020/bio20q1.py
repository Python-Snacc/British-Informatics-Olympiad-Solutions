"""
Q1s are usually not this implementation-heavy, but here we are.
I think you just have to be rigorous for this, and I found it was easiest to split up the look and say functions.
While it is a bit long, each step is very simple, so I haven't commented them.
Please do let me know if you have a shorter solution, though!
"""


def look(_roman_numeral):
    current_letter = None
    letters = []
    occurrences = []
    for x in _roman_numeral:
        if x != current_letter:
            current_letter = x
            letters.append(current_letter)
            occurrences.append(1)
        else:
            occurrences[-1] += 1
    return letters, occurrences


def roman_numeral(n):
    string = ""
    thousands = n//1000
    string += "M" * thousands
    n -= thousands * 1000
    if n >= 900:
        string += "CM"
        n -= 900
    if n >= 500:
        string += "D" 
        n -= 500
    if n >= 400:
        string += "CD"
        n -= 400
    hundreds = n//100
    string += "C" * hundreds
    n -= hundreds * 100
    if n >= 90:
        string += "XC"
        n -= 90
    if n >= 50:
        string += "L"
        n -= 50
    if n >= 40:
        string += "XL"
        n -= 40
    tens = n//10
    string += "X" * tens
    n -= tens * 10
    if n == 9:
        string += "IX"
        return string
    if n >= 5:
        string += "V"
        n -= 5
    if n == 4:
        string += "IV"
        return string
    units = n
    string += "I" * units
    return string


def say(letters, occurrences):
    string = ""
    for i in range(len(letters)):
        string += roman_numeral(occurrences[i]) + letters[i]
    return string


def look_and_say(numeral, n):
    n = int(n)
    for i in range(n):
        letters, occurrences = look(numeral)
        numeral = say(letters, occurrences)
    iCount = 0
    vCount = 0
    for letter in numeral:
        if letter == "I":
            iCount += 1
        elif letter == "V":
            vCount += 1
    print(f"{iCount} {vCount}")
    return numeral


order = ["I", "V", "X", "L", "C", "D", "M"]


def valid(roman_numeral):
    if "IC" in roman_numeral or "IM" in roman_numeral or "IL" in roman_numeral or "ID" in roman_numeral or roman_numeral == "IIX":
        return False
    for i in range(len(roman_numeral)-3):
        if roman_numeral[i] == roman_numeral[i+1] == roman_numeral[i+2] == roman_numeral[i+3]:
            return False
        if order.index(roman_numeral[i + 3]) > order.index(roman_numeral[i]):
            return False
        if roman_numeral[i] == "I" and (roman_numeral[i+1] == "X" or roman_numeral[i+1] == "V") and roman_numeral[i+2] == "I":
            return False
        if roman_numeral[i] == "I" and roman_numeral[i+1] == "I" and (roman_numeral[i+2] == "V" or roman_numeral[i+2] == "X" or roman_numeral[i+2] == "C" or roman_numeral[i+2] == "M"):
            return False
        if roman_numeral[i+1] == "I" and (roman_numeral[i+2] == "X" or roman_numeral[i+2] == "V") and roman_numeral[i+3] == "I":
            return False
        if roman_numeral[i+1] == "I" and roman_numeral[i+2] == "I" and (roman_numeral[i+3] == "V" or roman_numeral[i+3] == "X" or roman_numeral[i+3] == "C" or roman_numeral[i+3] == "M"):
            return False
    else: return True


def b():
    for i in range(1,4000):
        temp = look_and_say(roman_numeral(i),1)
        if valid(temp):
            print(temp)


def c():
    lst = []
    for i in range(1,4000):
        temp = look_and_say(roman_numeral(i),1)
        if temp not in lst:
            lst.append(temp)
    print(len(lst))


if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        print("\n")
        numeral, n = input().split()
        look_and_say(numeral, n)
