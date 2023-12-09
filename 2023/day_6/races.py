import math

with open('input.txt', 'r') as file:
    lines = file.readlines()

times, distances = [[int(t) for t in l.split(':')[1].split()] for l in lines]

ways = [0 for _ in times]

for i, t in enumerate(times):
    for hold in range(t):
        distance = hold * (t - hold)

        if distance >= distances[i]: ways[i] += 1

print(math.prod(ways))
