# For each game
#   Find the fewest number of cubes of each color
#   that could have been in the bag to make the game possible.
#   Compute the power of this set of cubes
#   which is equal to the numbers of red, green, and blue cubes
#   multiplied together.
# Return the sum of all the power results.

# Possible colors for a cube
colors = ['red', 'green', 'blue']

# Read the document and get lines as a list of strings
document = 'input.txt'
with open(document, 'r') as file:
    lines = file.readlines()

# Initialize the sum of the power of cubes which will be returned at the end
sum_of_power_of_cubes = 0

for line in lines:
    # Initialize a parsed game list (holding grabs)
    # of dictionaries (holding cubes' color and value)
    game = []

    # Split the line in grabs (list of substrings)
    # like [' 10 green, 5 blue', ' 1 red, 9 green, 10 blue']
    grabs = line.split(':')[1].split(';')

    for grab in grabs:
        # ------------------------------
        # Parse the game (list of dictionaries)
        # ------------------------------

        # Split grabs in color-value pairs
        pairs = grab.split(',')

        # Initialize and reset on each iteration of grabs
        # a cubes dictionary holding color-value pairs
        # present in a grab
        cubes = {}

        for pair in pairs:
            # Split value and color
            count = int(pair.strip().split(' ')[0])
            color = pair.strip().split(' ')[1]

            # Add the key value pair to the tmp cubes dictionary
            cubes[color] = count

        # Add the new cubes dictionary to the game list
        game.append(cubes)

    # ------------------------------
    # Now the game is parsed (list of dictionaries)
    # ------------------------------

    # Initialize a dictionary to store the fewest number of cubes of each color
    # that could have been in the bag to make the game possible
    fewest_number_of_cubes = {}

    # Iterate inside the list and the dictionaries
    #   FOR each possible color, IF color is in the dictionary
    #       IF color is already in fewest_number_of_cube
    #       OR color value is greater than color value from the dictionary
    #           Add or replace the value in the dictionary
    for grab in game:
        for index, color in enumerate(colors):
            if color in grab:
                if (color not in fewest_number_of_cubes or
                    grab[color] > fewest_number_of_cubes[color]):

                    fewest_number_of_cubes[color] = grab[color]

    # Compute the power of a set of cubes
    # which is equal to the numbers of red, green, and blue cubes
    # multiplied together
    power_of_cubes = 1
    for value in fewest_number_of_cubes.values():
        power_of_cubes *= value

    # Add the result to the total sum
    sum_of_power_of_cubes += power_of_cubes

print(sum_of_power_of_cubes)
