import os
import sys
import math

class Crab:
    def __init__(self, pos):
        self.pos = pos

    def __str__(self):
        return f"{self.pos}"

    def __int__(self):
        return self.pos


def main():
    filepath = os.path.join(os.getcwd(), "input.txt")
    with open(filepath) as file:
        input = map(int, file.read().split(","))
        crabs = [int(element) for element in input]

    nums = list(range(min(crabs), max(crabs)))
    pivot_costs = {}
    for pivot in nums:
        pivot_cost = 0
        for crab in crabs:
            n = abs(pivot - crab)
            cost = (n*(n+1))/2
            pivot_cost += cost
        pivot_costs[pivot] = pivot_cost
        #print(f"Setting pivot {pivot} to cost {pivot_cost}")

    print(min(pivot_costs.values()))

if __name__ == "__main__":
    main()