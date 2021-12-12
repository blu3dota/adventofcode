import os
import sys


def main():
    fish_classes = []
    for i in range(9):
        fish_classes.append(0)

    filepath = os.path.join(sys.path[0], "input.txt")
    with open(filepath) as file:
        for timer in map(int, file.read().split(",")):
            fish_classes[timer] += 1

    print(f"{fish_classes} {sum(fish_classes)}")
    for i in range(256):
        simulate(fish_classes)
        print(f"Day {i+1}: {fish_classes} {sum(fish_classes)}")

def simulate(fish):
    new_fish = 0
    wrap = 0
    for i,f in enumerate(fish):
        if i == 0:
            new_fish = f
            wrap = f
            continue
        fish[i-1] = fish[i]
    fish[6] += wrap
    fish[8] = new_fish

if __name__ == "__main__":
    main()
