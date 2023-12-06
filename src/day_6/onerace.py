with open('input.txt', 'r') as file:
    lines = file.readlines()

time, distance = [int(''.join(l.split(':')[1].split())) for l in lines]

ways = 0

for hold in range(time):
    distance_with_boat = hold * (time - hold)

    if distance_with_boat >= distance: ways += 1

print(ways)
