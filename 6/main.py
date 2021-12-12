import os
import sys


class Fish:
    def __init__(self, timer=8):
        self.timer = timer

    def simulate(self, days, swarm):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            swarm.append(Fish(8))


def main():
    filepath = os.path.join(sys.path[0], "input.txt")
    fish = []
    with open(filepath) as file:
        for timer in map(int, file.read().split(",")):
            fish.append(Fish(timer))

    simulate(80, fish)
    print(len(fish))

def simulate(days, fish):
    new_fish = []
    for i in range(days):
        for f in fish:
            f.simulate(1, new_fish)
        print(f"Simulating day {i}")
        fish.extend(new_fish)
        new_fish.clear()

if __name__ == "__main__":
    main()
