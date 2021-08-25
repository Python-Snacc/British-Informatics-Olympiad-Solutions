string = input()

def block_palindrome(string):
    blocks = 0
    for i in range(1, len(string)//2+1):
        if (string[:i] == string[-i:]):
            blocks += 1 + block_palindrome(string[i:-i])
    return blocks

NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")
print(block_palindrome(string))
