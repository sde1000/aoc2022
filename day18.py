#!/usr/bin/env python3

with open("day18-input.txt") as f:
    cubes = set(tuple(int(x) for x in line.split(',')) for line in f)


def neighbours(cube):
    x, y, z = cube
    return [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z),
            (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]


print(f"Part 1: "
      f"{sum(n not in cubes for cube in cubes for n in neighbours(cube))}")

xs = {x for x, y, z in cubes}
ys = {y for x, y, z in cubes}
zs = {z for x, y, z in cubes}

all_cubes = frozenset(
    (x, y, z)
    for x in range(min(xs) - 1, max(xs) + 2)
    for y in range(min(ys) - 1, max(ys) + 2)
    for z in range(min(zs) - 1, max(zs) + 2)
)

air = all_cubes.difference(cubes)

outside = set()
new_members = {(min(xs) - 1, min(ys) - 1, min(zs) - 1)}

while new_members:
    outside.update(new_members)
    new_members = set(
        n for cube in outside for n in neighbours(cube)
        if n in air and n not in outside)

print(f"Part 2: "
      f"{sum(n in outside for cube in cubes for n in neighbours(cube))}")
