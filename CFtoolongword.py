def abbreviate(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[-1]
    else:
        return word

# Read input
n = int(input())
words = [input() for _ in range(n)]

# Process words and print results
for word in words:
    print(abbreviate(word))
