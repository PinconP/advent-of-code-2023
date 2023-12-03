import re


def load_puzzle(path):
    # Initialize an empty list to store the lines
    lines = []

    # Open the file in read mode
    with open(path, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Strip newline characters and append the line to the list
            lines.append(line.strip())

    # Now lines contains all the lines from the file
    return lines


def extract_digits_final(s):
    # Extensive dictionary mapping spelled out numbers to their digit equivalents
    number_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # Compiling a regular expression pattern for better matching
    pattern = re.compile(r"(" + "|".join(number_map.keys()) + r"|\d)")

    # List to hold the extracted digits
    extracted_digits = []

    # Iterating over the matches
    for match in pattern.finditer(s):
        word = match.group()
        # If the word is a spelled out number, convert it to digit
        if word in number_map:
            extracted_digits.append(number_map[word])
        # If the word is a digit, add it directly
        elif word.isdigit():
            extracted_digits.append(int(word))
    return extracted_digits


class Day01:
    def __init__(self, path):
        # Load the puzzle from the file
        self.puzzle = load_puzzle(path)
        # Initialize the solution to None
        self.solution = None

    def solve(self):
        # Split the text into lines
        lines = self.puzzle

        # Initialize the total sum
        total_sum = 0

        # Iterate over each line
        for line in lines:
            # Extract all digits from the line
            digits = extract_digits_final(line)

            line_sum = int("".join([str(digits[0]), str(digits[-1])]))

            # Add the sum of the current line to the total sum
            total_sum += line_sum

        self.solution = total_sum


if __name__ == "__main__":
    # Create a new puzzle instance
    puzzle = Day01("src/Day01/puzzle_test.txt")

    # Solve the puzzle
    puzzle.solve()

    # Print the solution
    print(puzzle.solution)
