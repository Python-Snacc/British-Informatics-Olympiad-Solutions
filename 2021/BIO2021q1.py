from string import ascii_uppercase
from functools import lru_cache
from itertools import permutations


# We cache results of the pat() function since we will need to reuse the same strings multiple times.
# We could implement our own memoization, or we can just use lru_cache.
@lru_cache(maxsize=None)
def pat(word):
    if len(word) == 1:  # A word of length one is definitely a pat.
        return True

    # Check all possible splits of the word.
    for i in range(len(word) - 1):
        left = word[:i + 1]
        right = word[i + 1:]

        """
        We want to check if every letter in left is smaller (lexicographically) than every letter in right.
        For this problem, it is sufficient to do this in O(n^2):
        if all(x > y for y in right for x in left)
        
        However, we can do this in O(n): 
        We just need to find whether the smallest letter of left is larger than the largest of right!
        """

        if min(left) > max(right):
            if pat(left[::-1]) and pat(right[::-1]):
                return True

    return False


def solve():
    s1, s2 = input().split()
    print("YES" if pat(s1) else "NO")
    print("YES" if pat(s2) else "NO")
    print("YES" if pat(s1 + s2) else "NO")


def b():
    p = ["".join(s) for s in permutations("ABCD")]
    for string in p:
        if pat(string):
            print(string)


# A modified version of the pat() function.
# Counts the number of pats in a given word.
@lru_cache(maxsize=None)
def num_pats(word):
    if len(word) == 1:
        return 1

    ans = 0
    # Check all possible splits of the word.
    for i in range(len(word) - 1):
        left = word[:i + 1]
        right = word[i + 1:]
        if min(left) > max(right):
            if pat(left[::-1]) and pat(right[::-1]):
                ans += 1

    return ans


def c():
    # We can check the number of pats up to a couple of letters using num_pats and permutations.
    # While you could realise that they are simply the Catalan Numbers,
    # let's make a recurrence relation to solve this problem without knowledge of them!
    #
    # Let P[i] be the number of pats using i+1 letters.
    # P[n+1] = Sum of P[i]P[n-i] for all i between 0 and n inclusive.
    # (i.e. using the first i letters and then the next n-i letters,
    #       since the right part must use larger letters than the left.)
    #
    # We can ignore A because, for any pat starting with B made of letters B...Z,
    # there is only one place that the A can go such that the resulting word is also a pat.
    # Therefore, we want P[23].

    P = [0 for _ in range(24)]
    P[0] = 1
    for n in range(23):
        for i in range(0, n+1):
            P[n+1] += P[i] * P[n-i]

    print(P[23])  # 343059613650


if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    solve()
