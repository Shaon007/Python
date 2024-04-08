def min_cost(t, test_cases):
    for n, a, b in test_cases:
        if a <= b / 2:  # Cheaper to buy individually
            cost = n * a
        else:  # Cheaper to buy in pairs on promotion
            pairs = n // 2
            singles = n % 2
            cost = pairs * b + singles * a
        print(cost)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, a, b = map(int, input().split())
    test_cases.append((n, a, b))

# Calculate and output minimum cost
min_cost(t, test_cases)
