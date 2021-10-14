import numpy as np


class Square:
    def __init__(self):
        self.array = np.full((3, 3), {1, 2, 3, 4, 5, 6, 7, 8, 9})

    def __str__(self):
        return str(self.array)


class Game:
    def __init__(self):
        self.board = np.empty((3, 3), dtype=Square)

        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                self.board[row][col] = Square()
                print("self.board: ", self.board)

        # self.board[:][:] = Square()
        print("Initial board: ", self.board)

    def __str__(self):
        ret_string = ""

        for row in self.board:
            square_0 = row[0].array
            square_1 = row[1].array
            square_2 = row[2].array

            for i in range(3):
                ret_string += str(square_0[:][i]) + "\t" + str(square_1[:][i]) + "\t" + str(square_2[:][i]) + "\n"

            # for square in row:
            #     ret_string += str(square) + "\t"
            ret_string += "\n"

        return ret_string


def print_hi(name):
    my_game = Game()
    print(my_game)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
