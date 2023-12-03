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
