import os

octos = []
dim = -1
flashed = []
global_flashes = 0


def check_all_flashed():
    global octos, flashed, global_flashes

    for i,e in enumerate(octos):
        for j,x in enumerate(octos[i]):
            if octos[i][j] != 0:
                return False

    return True


def main():
    global dim
    filename = os.path.join(os.getcwd(), "input.txt")
    with open(filename) as file:
        for line in file.read().splitlines():
            octos.append(list(map(int, list(line))))
    dim = len(octos[0])

    round = 0
    while check_all_flashed() == False:
        step()
        round += 1

    print(round)

def flash(i, j):
    global octos, flashed, global_flashes
    octos[i][j] = 0

    for add_i in [-1, 0, 1]:
        for add_j in [-1, 0, 1]:
            if i + add_i >= 0 and i + add_i < dim and j + add_j >= 0 and j + add_j < dim and (add_i, add_j) != (0, 0) and (i + add_i, j + add_j) not in flashed:
                octos[i + add_i][j + add_j] += 1

    global_flashes += 1

def step():
    global octos, flashed, global_flashes
    for i,e in enumerate(octos):
        for j,x in enumerate(octos[i]):
            octos[i][j] += 1

    flashed = []
    while True:
        flashcount = 0
        for i, e in enumerate(octos):
            for j, x in enumerate(octos[i]):
                if octos[i][j] > 9 and (i, j) not in flashed:
                    flashed.append((i, j))
                    flashcount += 1
                    flash(i, j)

        if (flashcount == 0):
            break

    #for line in octos:
    #    print(line)
    #print("----")

if __name__ == "__main__":
    main()