
def createSecondDial(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second_Dial = ""
    a = -1
    used = ""
    for i in range(26):
        a += n
        a %= 26-i
        second_Dial += alphabet[a]
        alphabet = alphabet.replace(alphabet[a], "")
        a -= 1
    return second_Dial

def encrypt(string, second_Dial):
    encrypted = ""
    first_Dial = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(string)):
        encrypted += second_Dial[(first_Dial.index(string[i])+i)%26]
    return encrypted
        
def c():
    for i in range(1,1000001):
        second_Dial = createSecondDial(i)
        x = encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", second_Dial)
        if sorted(x) == list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            print(second_Dial)
if __name__ == '__main__':
    print("Name: Ryuichi Leo Takashige\nSchool: Westminster School\n")
    n, string = input().split()
    second_Dial = createSecondDial(int(n))
    print(second_Dial[:6])
    print(encrypt(string, second_Dial))



"""

def createSecondDial2(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second_Dial = ""
    a = -1
    used = ""
    for i in range(26):
        for _ in range(n):
            a += 1
            a%=26
            while alphabet[a] in used:
                a+=1
                a%=26
        second_Dial += alphabet[a]
        used += alphabet[a]
    return second_Dial

"""
