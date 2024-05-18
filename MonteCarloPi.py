import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        # Generate random point (x, y) in the square [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the circle with radius 1
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Estimate Pi using the ratio of points inside the circle to total points
    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

# Number of points to simulate
num_points = 1000000

# Estimate Pi
pi_estimate = estimate_pi(num_points)
print(f"Estimated value of Pi: {pi_estimate}")
