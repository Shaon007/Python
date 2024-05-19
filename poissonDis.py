import math

def poisson_probability(lmbda, k):

    log_p = k * math.log(lmbda) - lmbda - math.lgamma(k + 1)
    return math.exp(log_p)

def main():
    # Get number of test cases
    num_cases = int(input("Enter the number of test cases: "))

    # Collect input for each test case
    cases = []
    for i in range(num_cases):
        if i != 0:
            print()  # Print a blank line between input prompts for different cases
        lmbda = float(input("Enter the average number of events: "))
        k = int(input("Enter the estimated number of events: "))
        cases.append((lmbda, k))

    # Calculate and print the probabilities for each case
    for lmbda, k in cases:
        probability = poisson_probability(lmbda, k)
        print(f"{probability:.6f}")

if __name__ == "__main__":
    main()
