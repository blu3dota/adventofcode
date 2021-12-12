import os
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
value_file = "input.txt"

def main():
    values = []
    file = open_file(__location__, value_file)
    increases = 0

    values.append(int(file.readline()))
    values.append(int(file.readline()))
    values.append(int(file.readline()))

    file.seek(0)
    file.readline() # Skip first 3 line
    file.readline()
    file.readline()

    for line in file:
        current_sum = sum(values)
        # debug_output = values.copy()
        values.pop(0)
        values.append(int(line))
        next_sum = sum(values)

        if (next_sum > current_sum):
            increases+=1

        #print("{} {} -> {}".format(debug_output, values, next_sum > current_sum))

    print("Increases: {}".format(increases))

def open_file(file_path, file_name):
    full_path = os.path.join(file_path, file_name)
    file = open(full_path)
    return file

if __name__ == "__main__":
    main()
