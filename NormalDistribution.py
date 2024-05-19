import math

# Given data
data = [67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49, 78, 77,
        83, 47, 67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49]

# Number of bins for the chi-square test
num_bins = 6

# Calculate observed frequencies
min_data, max_data = min(data), max(data)
bin_width = (max_data - min_data) / num_bins
bins = [min_data + i * bin_width for i in range(num_bins + 1)]
observed_frequencies = [0] * num_bins

for value in data:
    for i in range(num_bins):
        if bins[i] <= value < bins[i + 1]:
            observed_frequencies[i] += 1
            break
        elif value == max_data:  # Include the maximum value in the last bin
            observed_frequencies[-1] += 1

# Calculate mean and standard deviation
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

# Calculate expected frequencies
expected_frequencies = []
for i in range(num_bins):
    lower_bound = (bins[i] - mean) / std_dev
    upper_bound = (bins[i + 1] - mean) / std_dev
    expected_prob = (math.erf(upper_bound / math.sqrt(2)) - math.erf(lower_bound / math.sqrt(2))) / 2
    expected_frequencies.append(expected_prob * len(data))

# Chi-square test statistic
chi_square_statistic = sum(((observed_frequencies[i] - expected_frequencies[i]) ** 2) / expected_frequencies[i] for i in range(num_bins))

# Degrees of freedom: number of bins - 1 - number of parameters estimated (mean and std_dev)
degrees_of_freedom = num_bins - 1 - 2

# Significance level and critical value from chi-square distribution table (approximation)
alpha = 0.24
critical_value = 17.535  # Pre-calculated or from table for df=3 at alpha=0.24

# Output results
print("Observed Frequencies:", observed_frequencies)
print("Expected Frequencies:", expected_frequencies)
print("Chi-Square Statistic:", chi_square_statistic)
print("Degrees of Freedom:", degrees_of_freedom)
print("Critical Value:", critical_value)

if chi_square_statistic < critical_value:
    print("Fail to reject the null hypothesis: Data fits the normal distribution")
else:
    print("Reject the null hypothesis: Data does not fit the normal distribution")
