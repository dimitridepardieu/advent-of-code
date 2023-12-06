# Read almanach
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Find source numbers
source = lines[0].split(':')[1].split()
source = [int(i) for i in source]

# Initialize destination numbers (default to source)
destination = list(source)

# Keyword used to dissociate maps in the almanach
keyword = 'map'

for index, line in enumerate(lines):
    if keyword in line:
        # New source equals previous destination
        source = list(destination)
        # Reset destination
        destination = list(source)

    # Convert numbers from source to destination
    if line[0].isdigit():
        numbers = line.split()
        destination_range_start = int(numbers[0])
        source_range_start = int(numbers[1])
        range_length = int(numbers[2])

        # Compute key number used to map a source value to a destination value
        key = source_range_start - destination_range_start

        # Find destination value
        for index, n in enumerate(source):
            if n == source[index]:
                if n in range(source_range_start, source_range_start + range_length):
                    destination[index] = n - key

location = list(destination)

print(min(location))
