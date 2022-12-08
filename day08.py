#!/usr/bin/env python3

with open("day08-input.txt") as f:
    puz = f.read().split("\n")[:-1]

width = len(puz[0])
height = len(puz)
trees = [ int(c) for row in puz for c in row ]

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)


def coords(start, vector):
    y, x = start
    while y < height and x < width \
          and y >= 0 and x >= 0:
        yield y * width + x
        y = y + vector[0]
        x = x + vector[1]


def visible_from(start, vector):
    current_height = -1
    for c in coords(start, vector):
        if trees[c] > current_height:
            yield c
            current_height = trees[c]


def visible():
    visible_set = set()

    for x in range(width):
        visible_set.update(visible_from((0, x), down))
        visible_set.update(visible_from((height - 1, x), up))
    for y in range(height):
        visible_set.update(visible_from((y, 0), right))
        visible_set.update(visible_from((y, width - 1), left))

    return len(visible_set)


def viewing_distance(start, vector):
    cs = coords(start, vector)
    max_height = trees[next(cs)]
    d = 0
    for c in cs:
        d = d + 1
        if trees[c] >= max_height:
            break
    return d


def score(pos):
    return viewing_distance(pos, up) \
        * viewing_distance(pos, right) \
        * viewing_distance(pos, down) \
        * viewing_distance(pos, left)


def inner_trees():
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            yield (y, x)


print(f"Part 1: {visible()}")
print(f"Part 2: {max(score(pos) for pos in inner_trees())}")
