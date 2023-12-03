import unittest
import os
from src.Day01.day01 import Day01


class TestDay01(unittest.TestCase):
    test_data_dir = "test_data"  # Directory where test files will be stored

    @classmethod
    def setUpClass(cls):
        # Create a directory for test data if it doesn't exist
        os.makedirs(cls.test_data_dir, exist_ok=True)
        # Create test files
        cls.create_test_file(
            "test1.txt", ["one 3", "two 4", "five 9"]
        )  # Expected sum: 96
        cls.create_test_file("test2.txt", ["seven 1", "six 5"])  # Expected sum: 136
        cls.create_test_file("empty.txt", [])  # Expected sum: 0

    @classmethod
    def tearDownClass(cls):
        # Clean up: remove test files
        for filename in os.listdir(cls.test_data_dir):
            os.remove(os.path.join(cls.test_data_dir, filename))
        # Remove test directory
        os.rmdir(cls.test_data_dir)

    @classmethod
    def create_test_file(cls, filename, lines):
        # Create a test file with given lines
        with open(os.path.join(cls.test_data_dir, filename), "w") as file:
            for line in lines:
                file.write(line + "\n")

    def test_init(self):
        # Test the __init__ method
        puzzle = Day01(os.path.join(self.test_data_dir, "test1.txt"))
        self.assertIsNotNone(puzzle.puzzle)
        self.assertEqual(len(puzzle.puzzle), 3)

    def test_solve_with_data(self):
        # Test the solve method with data
        puzzle = Day01(os.path.join(self.test_data_dir, "test1.txt"))
        puzzle.solve()
        self.assertEqual(puzzle.solution, 96)

        puzzle = Day01(os.path.join(self.test_data_dir, "test2.txt"))
        puzzle.solve()
        self.assertEqual(puzzle.solution, 136)

    def test_solve_empty(self):
        # Test the solve method with empty file
        puzzle = Day01(os.path.join(self.test_data_dir, "empty.txt"))
        puzzle.solve()
        self.assertEqual(puzzle.solution, 0)


if __name__ == "__main__":
    unittest.main()
