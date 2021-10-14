import random
import numpy as np


class Square:
    def __init__(self):
        self.array = np.full((3, 3), {1, 2, 3, 4, 5, 6, 7, 8, 9})

    def __str__(self):
        return str(self.array)

    # Concretize a random value in this square
    def concretize_random_value(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)

            if len(self.array[i][j]) == 1:  # if the set possible values is just 1 then find another value
                continue
            else:
                # Pick a random value from the set of possibilities
                self.array[i][j] = {random.choice(tuple(self.array[i][j]))}
                return i, j

    # Check to see if this square is solved
    def solved(self):
        for value in self.array.flatten():
            if len(value) != 1:
                return False
        return True


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

    # Concretize a random value in the board
    def concretize_random_value(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)

            if self.board[i][j].solved():
                continue
            else:
                square_i, square_j = self.board[i][j].concretize_random_value()
                return i, j, square_i, square_j

    # Check to see if the game board is completely solved
    def solved(self):
        for square in self.board.flatten():  # Check all the square to see if there are solved
            if square.solved() is False:
                return False

        return True

    # Update the lists of possible values based off a decision
    def update_board(self, game_i, game_j, square_i, square_j):
        pass

    def create_board(self):
        while self.solved() is False:
            game_i, game_j, square_i, square_j = self.concretize_random_value()
            self.update_board(game_i, game_j, square_i, square_j)


if __name__ == '__main__':
    my_game = Game()
    print(my_game)
    my_game.create_board()
    print(my_game)
