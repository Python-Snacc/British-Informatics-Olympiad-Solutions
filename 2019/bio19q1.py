def is_palindrome(n):
    if n[::-1] == n: return True
    else: return False

def next_palindrome(n):
    n+=1
    while True:
        strn = str(n)
        if is_palindrome(strn):
            return n
        b = True
        for i in range(len(strn)//2):
            if is_palindrome(strn):
                return int(strn)
            if b:
                if int(strn[i]) >= int(strn[-i-1]):
                    if i != 0:
                        temp = strn[:-i-1] + strn[i] + strn[-i:]
                    else: 
                        temp = strn[:-i-1] + strn[i]
                    strn = temp
                else:
                    n = int(strn)
                    x = 10 + int(strn[i]) - int(strn[-i-1])
                    n += x * 10**i
                    strn = str(n)
                    b = False
        n = int(strn)
                
                
def find_all_palindromes(stop):
    lst = []
    for i in range(0,stop):
        if is_palindrome(str(i)):
            lst.append(i)
    print(len(lst))
    ans = []
    for i in range(len(lst)):
        print(len(ans))
        for j in range(i,len(lst)):
            k = lst[i]+lst[j]
            if k > stop:
                break
            if k not in ans:
                ans.append(k)
    print(stop-len(ans))
    # Buffers at 90070 so stands to reason that the answer is 9030.
    

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        n = input()
        print(next_palindrome(int(n)))
