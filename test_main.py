from unittest import TestCase
from main import Game, Square


class TestGame(TestCase):
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
    def test_solved_false(self):
        my_square = Square()

        self.assertFalse(my_square.solved())

    def test_solved_true(self):
        my_square = Square()
        my_square.array[:][:] = {1}

        self.assertTrue(my_square.solved())
