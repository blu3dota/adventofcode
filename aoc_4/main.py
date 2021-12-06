import sys
import os
import copy

class Dealer:
    def __init__(self, numbers):
        self.numbers = numbers

class Board:
    def __init__(self, grid):
        self.grid = grid
        self.marks = copy.deepcopy(self.grid)
        self.winning_number = None
        self.won = False
        for rows in self.marks:
            for i, number in enumerate(rows):
                rows[i] = 0

    def play(self, dealer):
        numbers = dealer.numbers
        for num in numbers:
            self.submit_number(num)
            if self.won:
                break
        #print(f"Won {self.won} with number {self.winning_number}")

    def score(self):
        if self.won is False or self.winning_number is None:
            return 0
        unmarked_sum = 0
        for i,row in enumerate(self.grid):
            for j,number in enumerate(row):
                if self.marks[i][j] == 0:
                    unmarked_sum += int(number)
        return unmarked_sum * self.winning_number

    def submit_number(self, number):
        for i,row in enumerate(self.grid):
            for j,num in enumerate(row):
                if int(num) == int(number) and self.marks[i][j] == 0:
                    self.marks[i][j] = 1
                    self.won = self.check_win(i, j)
                    if self.won:
                        self.winning_number = int(number)
                    return

    def check_win(self, i, j):
        # horizontal
        won = True
        for number in range(5):
            if self.marks[number][j] == 0:
                won = False
        if won:
            return True

        # vertical
        won = True
        for number in range(5):
            if self.marks[i][number] == 0:
                return False

        return won

    def __str__(self):
        return str(self.grid)

def main():
    file = os.path.join(sys.path[0], "input.txt")
    f = open(file)

    dealer = Dealer(f.readline().rstrip('\n').split(","))
    boards = []
    current_grid = None
    for line in f:
        if line == '\n' or len(line) == 0:
            if current_grid is not None:
                boards.append(Board(current_grid))
            current_grid = []
        else:
            current_grid.append(line.split())

    for number in dealer.numbers:
        for board in boards:
            board.submit_number(number)
        win_score = check_boards_for_win(boards)
        if win_score is not None:
            print(f"Winning Score: {win_score}")
            return

def check_boards_for_win(boards):
    highest_score = 0
    winner = None
    for board in boards:
        if board.won:
            winner = board
            if board.score() > highest_score:
                highest_score = board.score()

    if winner is not None:
        print(board)
        return highest_score
    else:
        return None

if __name__ == "__main__":
    main()