class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def contains(self, val):
        return val in self.elements

    def __len__(self):
        return sum(self.elements.values())

# Sample usage
if __name__ == "__main__":
    q = int(input())
    multiset = Multiset()
    results = []

    for _ in range(q):
        operation, *args = input().split()
        if operation == "add":
            multiset.add(int(args[0]))
        elif operation == "remove":
            multiset.remove(int(args[0]))
        elif operation == "query":
            results.append(multiset.contains(int(args[0])))
        elif operation == "size":
            results.append(len(multiset))

    for result in results:
        print(result)
