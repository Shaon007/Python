class LCG:
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current = seed

    def next(self):
        self.current = (self.multiplier * self.current + self.increment) % self.modulus
        return self.current

# Parameters
seed = 27
multiplier = 17
increment = 43
modulus = 100

# Create an instance of the LCG
lcg = LCG(seed, multiplier, increment, modulus)

# Generate a sequence of random numbers
sequence_length = 10
random_sequence = [lcg.next() for _ in range(sequence_length)]

print(random_sequence)
