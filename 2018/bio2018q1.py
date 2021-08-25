import math

def calculator(interest, repay):

    amount = 10000
    total_repaid = 0

    while amount > 0:
        interest_month = math.ceil((interest / 100) * amount)
        amount += interest_month
        repaid = math.ceil((repay / 100) * amount)
        repaid = min(max(5000, repaid), amount)
        total_repaid += repaid
        amount -= repaid

    print("%.2f" % (total_repaid / 100))

def b():
    print(5)

def c():
    maxPaid = 0
    maxI = 0
    maxR = 0
    for i in range(0,101):
        for r in range(0,101):
            temp = calculator(i,r)
            if temp > maxPaid:
                maxPaid = temp
                maxI = i
                maxR = r
    print((maxI, maxR))

if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        i, r = (int(x) for x in input().split())
        calculator(i,r)
        
