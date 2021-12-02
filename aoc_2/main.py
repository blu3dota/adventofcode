import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
value_file = "input.txt"

class Submarine:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def print(self):
        print("X:{} Y:{}".format(self.x, self.y))

    def execute_statement(self, statement):
        split = statement.split()
        dir = split[0]
        val = int(split[1])
        if (dir == "forward"):
            self.move(val, 0)
        elif (dir == "backward"):
            self.move(-val, 0)
        elif (dir == "down"):
            self.move(0, val)
        elif (dir == "up"):
            self.move(0, -val)

def main():
    boat = Submarine(0, 0)

    inputfile = open(os.path.join(__location__, value_file))
    for line in inputfile:
        boat.execute_statement(line)

    boat.print()
    print(boat.x * boat.y)


if __name__ == "__main__":
    main()