from functools import lru_cache


# The only way that some plans repeat is when they have the same number of characters remaining,
# and the same last character on the prefix.
@lru_cache(maxsize=None)
def count(remaining_characters, last_char, last_char_count, max_char_count, letters):
    if last_char_count is not None and last_char_count > max_char_count:
        # impossible
        return 0
    elif remaining_characters == 0:
        return 1
    else:
        total = 0

        for i in range(letters):
            if last_char is not None and last_char == i:
                total += count(
                    remaining_characters - 1,
                    last_char,
                    last_char_count + 1,
                    max_char_count,
                    letters,
                )
            else:
                total += count(remaining_characters - 1, i, 1, max_char_count, letters)

        return total


NAME = ""
SCHOOL = ""
print(f"Name: {NAME}\nSchool: {SCHOOL}")

letters, max_adjacent, expected_length = tuple(int(x) for x in input().split(" "))

n = int(input())
prefix = []
last = None
last_count = 0

# Find the nth plan's prefix until the nth plan is constructed.
while len(prefix) < expected_length:
    for i in range(letters):
        # How many of the past letters (in a row) are the same as this one.
        _last_count = last_count + 1 if i == last else 1
        prefix.append(i)
        with_prefix = count(
            expected_length - len(prefix), i, _last_count, max_adjacent, letters
        )

        if with_prefix >= n:
            # this is the right prefix
            last = i
            last_count = _last_count
            break

        # This wasn't the right prefix.
        # So subtract the number of plans starting with this prefix from the number of plans we are searching for.
        n -= with_prefix
        prefix.pop()  # Getting rid of the prefix we temporarily added in this loop.

# Print the string that is currently stored in an array of ascii numbers.
print("".join(chr(i + ord("A")) for i in prefix))
