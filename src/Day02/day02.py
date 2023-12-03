from src.load_puzzle import load_puzzle


class Day02:
    def __init__(self, path):
        self.puzzle = load_puzzle(path)
        self.solution_possibility = None
        self.solution_power = None
        self.red_limit = 12
        self.green_limit = 13
        self.blue_limit = 14

    def is_game_possible(self, game_data):
        if not game_data.strip():
            return True  # Assuming an empty game data means no cubes, hence the game is possible

        reveals = game_data.split("; ")
        for reveal in reveals:
            cubes = reveal.split(", ")
            red, green, blue = 0, 0, 0
            for cube in cubes:
                if cube:  # Check if cube is not an empty string
                    count, color = cube.split(" ")
                    count = int(count)
                    if color == "red":
                        red += count
                    elif color == "green":
                        green += count
                    elif color == "blue":
                        blue += count

            if (
                red > self.red_limit
                or green > self.green_limit
                or blue > self.blue_limit
            ):
                return False
        return True

    def minimum_cubes_and_power(self, game_data):
        if not game_data.strip():
            return 0  # Assuming an empty game data means no cubes, so the power is 0

        total_red, total_green, total_blue = 0, 0, 0
        reveals = game_data.split("; ")
        for reveal in reveals:
            cubes = reveal.split(", ")
            red, green, blue = 0, 0, 0
            for cube in cubes:
                if cube:  # Check if cube is not an empty string
                    count, color = cube.split(" ")
                    count = int(count)
                    if color == "red":
                        red = max(red, count)
                    elif color == "green":
                        green = max(green, count)
                    elif color == "blue":
                        blue = max(blue, count)
            total_red = max(total_red, red)
            total_green = max(total_green, green)
            total_blue = max(total_blue, blue)

        power = total_red * total_green * total_blue
        return power

    def solve_possibility(self):
        total_sum = 0
        for line in self.puzzle:
            game_id, game_data = line.split(": ")
            game_id = int(game_id.replace("Game ", ""))
            if self.is_game_possible(game_data):
                total_sum += game_id
        self.solution_possibility = total_sum

    def solve_power(self):
        total_power_sum = 0
        for line in self.puzzle:
            _, game_data = line.split(": ")
            power = self.minimum_cubes_and_power(game_data)
            total_power_sum += power
        self.solution_power = total_power_sum


# Create an instance of Day02 with the given puzzle file
day02 = Day02("src/Day02/puzzle.txt")
# Solve and print the possibility solution
day02.solve_possibility()
print(day02.solution_possibility)
# Solve and print the power solution
day02.solve_power()
print(day02.solution_power)
