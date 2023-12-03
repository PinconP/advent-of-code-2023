import unittest
from src.load_puzzle import load_puzzle
from src.Day02.day02 import Day02


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "src/Day02/puzzle_test.txt"
        self.day02 = Day02(self.test_file_path)

    def test_initialization(self):
        self.assertIsNotNone(
            self.day02.puzzle, "Puzzle should be loaded during initialization"
        )

    def test_is_game_possible(self):
        self.assertTrue(
            self.day02.is_game_possible("3 red, 5 green, 4 blue; 1 red, 2 green")
        )
        self.assertFalse(self.day02.is_game_possible("13 red, 5 green, 4 blue"))
        self.assertFalse(self.day02.is_game_possible("3 red, 14 green, 4 blue"))
        self.assertFalse(self.day02.is_game_possible("3 red, 5 green, 15 blue"))
        self.assertTrue(self.day02.is_game_possible(""))

    def test_minimum_cubes_and_power(self):
        self.assertEqual(
            self.day02.minimum_cubes_and_power(
                "3 red, 5 green, 4 blue; 1 red, 2 green"
            ),
            60,
        )
        self.assertEqual(self.day02.minimum_cubes_and_power("3 red"), 0)
        self.assertEqual(self.day02.minimum_cubes_and_power(""), 0)

    def test_solve_possibility(self):
        self.day02.solve_possibility()
        expected_sum = 8  # Value given in the instructions
        self.assertEqual(self.day02.solution_possibility, expected_sum)

    def test_solve_power(self):
        self.day02.solve_power()
        expected_power_sum = 2286  # Value given in the instructions
        self.assertEqual(self.day02.solution_power, expected_power_sum)


if __name__ == "__main__":
    unittest.main()
