import pickle

coins = [- 2**i for i in range(25)]
coins2 = [-i for i in coins]
def solve(start, end):
    len_primes = len(primes)
    lst = [0 for _ in range(len_primes)]
    lst[pos[start]] = 1
    for i in range(pos[start], pos[end]+1):
        c=primes[i]
        for coin in coins2:
            if coin>c:
                #print(c)
                break
            if c-coin not in primes:
                #print(c)
                continue
            if lst[pos[c-coin]]==0:
                continue
            if lst[i]==0:
                lst[i]=lst[pos[c-coin]]+1
                continue
            lst[i]=min(lst[pos[c-coin]]+1, lst[i])
    for i in range(pos[start], pos[end]+1):
        c=primes[i]
        if c==29: print(c)
        for coin in coins:
            if c==29 and coin==-2:
                print(c-coin)
            if c-coin>l-1:
                #print(c)
                continue
            if c-coin not in primes:
                #print(c)
                continue
            if lst[pos[c-coin]]==0:
                continue
            if lst[i]==0:
                lst[i]=lst[pos[c-coin]]+1
                continue
            lst[i]=min(lst[pos[c-coin]]+1, lst[i])

    print(primes)
    print(lst)
    print(lst[pos[end]])


if __name__=='__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    l, p, q = (int(x) for x in input().split())
    with open("Primes.pickle", 'rb') as f:
        primes = [int(x) for x in pickle.load(f) if int(x) < l]
    pos = {primes[i]:i for i in range(len(primes))}
    solve(p,q)
