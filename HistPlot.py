import numpy as np
import matplotlib.pyplot as plt

# Given ages of newborn babies
ages = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5]

# Constructing the frequency distribution table
unique_ages, counts = np.unique(ages, return_counts=True)

# Plotting the histogram
plt.figure(figsize=(8, 6))
plt.bar(unique_ages, counts, color='skyblue')
plt.title('Histogram of Newborn Babies Ages')
plt.xlabel('Age in Days')
plt.ylabel('Frequency')
plt.xticks(unique_ages)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
