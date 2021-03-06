import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
value_file = "input.txt"

class Submarine:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self.aim = aim

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return "X:{} Depth:{} Aim:{}".format(self.x, self.y, self.aim)

    def execute_statement(self, statement):
        split = statement.split()
        dir = split[0]
        val = int(split[1])
        if (dir == "forward"):
            self.move(val, self.aim * val)
        elif (dir == "down"):
            self.aim += val
        elif (dir == "up"):
            self.aim -= val

def main():
    boat = Submarine(0, 0, 0)

    inputfile = open(os.path.join(__location__, value_file))
    for line in inputfile:
        boat.execute_statement(line)

    print(boat)
    print(boat.x * boat.y)


if __name__ == "__main__":
    main()