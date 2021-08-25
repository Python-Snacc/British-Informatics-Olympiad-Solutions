from time import time
from itertools import combinations_with_replacement as cr

pairs = {"RR":"R","GG":"G","BB":"B", "RG":"B", "GR":"B","BR":"G", "RB":"G","GB":"R","BG":"R"}

def finalColour(string):
    if len(string)==1:
        return string
    while len(string) > 1:
        temp = ""
        for i in range(len(string)-1):
            temp += pairs[string[i] + string[i+1]]
        string = temp
    return string

def createRow(length, middle):
    # With chosen extreme left and right
    string = "B" + middle + "B"

def d():
    colours = ["B","R","G"]
    i = 4
    while True:
        i += 1
        b = True
        for x in cr(colours, i-2):
            print("".join(x))
            if not b:
                break
            string = "B" + "".join(x) + "B"
            if finalColour(string) != "B":
                b= False
        if b:
            print(i)
            break

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        print("\n")
        string = input()
        # start = time()
        print(finalColour(string))
        # print(time()-start)
