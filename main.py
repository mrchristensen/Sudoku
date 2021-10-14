import random
import numpy as np

infinity = 10  # Infinite weight because the most possible entropy will be 9


class Square:
    def __init__(self):
        self.array = np.empty((3, 3), dtype=set)

        for i in range(3):
            for j in range(3):
                self.array[i][j] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __str__(self):
        return str(self.array)

    def get_lowest_entropy_index(self):
        lowest_found_entropy = infinity
        square_i, square_j = None, None

        for i in range(3):
            for j in range(3):
                entropy = len(self.array[i][j])

                if 1 < entropy < lowest_found_entropy:
                    lowest_found_entropy = entropy
                    square_i = i
                    square_j = j

        return lowest_found_entropy, square_i, square_j

    # Concretize a random value in this square
    def colapse_value(self, i, j):
        self.array[i][j] = {random.choice(tuple(self.array[i][j]))}

    def remove_possible_value_from_square(self, value):
        for i in range(3):
            for j in range(3):
                if len(self.array[i][j]) > 1:
                    # print(self.array[i][j], value, i, j)
                    # print(self.array)
                    self.array[i][j].discard(value)

    def remove_possible_from_row(self, value, row):
        # print("value to remove: ", value, "row: ", row)
        # print("square before:")
        # print(self)
        for j in range(3):
            if len(self.array[row][j]) > 1:
                self.array[row][j].discard(value)
        # print("square after:")
        # print(self)

    def remove_possible_from_col(self, value, col):
        for i in range(3):
            if len(self.array[i][col]) > 1:
                self.array[i][col].discard(value)

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
                # print("self.board: ", self.board)

        # print("Initial board: ", self.board)

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
    def colapse_lowest_entropy_value(self):
        lowest_found_entropy = infinity
        game_i, game_j = None, None
        square_i, square_j = None, None

        for new_game_i in range(3):
            for new_game_j in range(3):
                new_entropy, new_square_i, new_square_j = self.board[new_game_i][new_game_j].get_lowest_entropy_index()

                # Find the spot with the fewest number of possible values (excluding cells that are already colapsed to a single value
                if lowest_found_entropy > new_entropy > 1:
                    print("new lowest entropy: ", new_entropy)
                    lowest_found_entropy = new_entropy
                    game_i = new_game_i
                    game_j = new_game_j
                    square_i = new_square_i
                    square_j = new_square_j

        self.board[game_i][game_j].colapse_value(square_i, square_j)
        return game_i, game_j, square_i, square_j

    # Check to see if the game board is completely solved
    def solved(self):
        for square in self.board.flatten():  # Check all the square to see if there are solved
            if square.solved() is False:
                return False

        return True

    # Update the lists of possible values based off a decision
    def update_board(self, game_i, game_j, square_i, square_j):
        new_concrete_value = list(self.board[game_i][game_j].array[square_i][square_j])[0]

        # Remove possible value from square
        self.board[game_i][game_j].remove_possible_value_from_square(new_concrete_value)

        # Update all values in rows and cols to not have that possible value
        for j in range(3):  # Remove rows
            self.board[square_i][j].remove_possible_from_row(new_concrete_value, game_i)

        for i in range(3):  # Remove rows
            self.board[i][square_j].remove_possible_from_col(new_concrete_value, game_j)

    def create_board(self):
        while self.solved() is False:
            game_i, game_j, square_i, square_j = self.colapse_lowest_entropy_value()
            self.update_board(game_i, game_j, square_i, square_j)
            print("Newly updateed board:")
            print(self)


if __name__ == '__main__':
    my_game = Game()
    print("Initial game board: ")
    print(my_game)
    my_game.create_board()
    print("Final game board: ")
    print(my_game)
