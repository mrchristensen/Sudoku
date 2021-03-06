from unittest import TestCase
from main import Game, Square


class TestGame(TestCase):
    def test_init(self):
        my_game = Game()
        print(my_game)

        my_game.board[0][0].array[0][2].remove(1)
        print(my_game)

        self.assertFalse(1 in my_game.board[0][0].array[0][2])
        self.assertTrue(1 in my_game.board[0][0].array[0][0])

    def test_solved_false(self):
        my_game = Game()
        self.assertFalse(my_game.solved())

    def test_solved_true(self):
        my_square = Square()
        my_square.array[:][:] = {1}

        my_game = Game()
        my_game.board[:][:] = my_square

        print(my_game)
        self.assertTrue(my_game.solved())


class TestSquare(TestCase):
    def test_init(self):
        my_square = Square()
        print(my_square)

        my_square.array[0][0].remove(1)
        print(my_square)

        self.assertFalse(1 in my_square.array[0][0])
        self.assertTrue(1 in my_square.array[1][1])

    def test_solved_false(self):
        my_square = Square()

        self.assertFalse(my_square.solved())

    def test_solved_true(self):
        my_square = Square()
        my_square.array[:][:] = {1}

        self.assertTrue(my_square.solved())

