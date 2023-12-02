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


class Puzzle:
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
            digits = [int(char) for char in line if char.isdigit()]
            # Calculate the calibration value for the line

            line_sum = int("".join([str(digits[0]), str(digits[-1])]))
            # Add the sum of the current line to the total sum
            total_sum += line_sum

        return total_sum


if __name__ == "__main__":
    # Create a new puzzle instance
    puzzle = Puzzle("puzzle")

    # Solve the puzzle
    solution = puzzle.solve()

    # Print the solution
    print(solution)
