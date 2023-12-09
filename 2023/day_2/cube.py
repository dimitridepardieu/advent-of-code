# Read file line by line to iterate through the games
#   Find game ID
#   Build list (holding grabs) of dictionaries (holding cubes)
#   Check if the bag contains max 12 red, 13 green, and 14 blue cubes
#       If game is valid add its ID to a list
# Return the sum the list of valid game IDs

# Possible colors for a cube
colors = ['red', 'green', 'blue']

# Number of cubes the bag contains
RED = 12
GREEN = 13
BLUE = 14
COLORS = [RED, GREEN, BLUE]

# Read the document and get lines as a list of strings
document = 'input.txt'
with open(document, 'r') as file:
    lines = file.readlines()

# List that will hold valid game IDs
ids = []

for line in lines:
    # Get game ID
    id = int(line.split(':')[0].split()[1])

    # Initialize a parsed game list (holding grabs)
    # of dictionaries (holding cubes' color and value)
    game = []

    # Parse game line in grabs
    # like [' 10 green, 5 blue', ' 1 red, 9 green, 10 blue']
    grabs = line.split(':')[1].split(';')

    for grab in grabs:
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

    # Now the game is parsed (list of dictionaries)

    # Count total and valid items in the list of dictionaries
    total_items = 0
    valid_items = 0

    # Iterate inside the list and the dictionaries
    #   For each possible color, if color is in the dictionary
    #       Add 1 to the total number of items
    #       If the color value is possible
    #           Add 1 to the total number of valid items
    for grab in game:
        for index, color in enumerate(colors):
            if color in grab:
                total_items += 1
                if grab[color] <= COLORS[index]:
                    valid_items += 1

    # If all items are valid, the game is valid
    # Add game ID to ids list
    if valid_items == total_items:
        # Add game ID to ids list
        ids.append(id)

# Print sum of all valid games IDs
print(sum(ids))
