import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
dictionary_name = "input.txt"

def main():
    file_location = os.path.join(__location__, dictionary_name)
    file = open(file_location)
    curNum = int(file.readline())
    incs = 0
    for line in file:
        nextNum = int(line)
        if nextNum > curNum:
            incs+=1
        curNum = nextNum
    print("Increments: {}".format(incs))

if __name__ == "__main__":
    main()


