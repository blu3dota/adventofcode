import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
value_file = "input.txt"

def main():
    inputfile = open(os.path.join(__location__, value_file))
    f = inputfile.readlines()

    output_number = []

    for x in range(len(f[0]) - 1):
        zeros = 0
        ones = 0
        for line in f:
          if (line[x] == '0'):
              zeros += 1
          else:
              ones += 1
        output_number.append('0' if zeros > ones else '1')

    first = int("".join(output_number), 2)
    for x in range(len(output_number)):
        if (output_number[x] == '0'):
            output_number[x] = '1'
        else:
            output_number[x] = '0'

    second = int("".join(output_number), 2)
    print(f"First: {first} Second: {second} Consumption: {first*second}")




if __name__ == "__main__":
    main()