import random

def simulate_double_six(num_simulations, num_rolls):
    double_six_count = 0

    for _ in range(num_simulations):
        for _ in range(num_rolls):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == 6 and dice2 == 6:
                double_six_count += 1
                break

    probability = double_six_count / num_simulations
    return probability

# Number of simulations
num_simulations = 100000
# Number of rolls in each simulation
num_rolls = 24

# Calculate the probability using simulation
simulation_probability = simulate_double_six(num_simulations, num_rolls)
print(f"Simulated probability of getting at least one double six in 24 rolls: {simulation_probability:.6f}")
