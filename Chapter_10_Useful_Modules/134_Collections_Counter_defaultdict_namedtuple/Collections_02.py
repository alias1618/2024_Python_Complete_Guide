from collections import Counter

letters = "aaaaaaaaaaaaaaabbbbbbbcccccccccddddddddddeeeeeeeeee"

c = Counter(letters)
print(c)
print(c.most_common(3))  # Most common 3 letters