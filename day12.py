#!/usr/bin/env python3

import heapq

heights = {}

with open("day12-input.txt") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, c in enumerate(row):
            if c == 'S':
                start = (y, x)
                c = 'a'
            elif c == 'E':
                end = (y, x)
                c = 'z'
            heights[(y, x)] = ord(c)


def neighbours(c):
    y, x = c
    yield (y - 1, x)
    yield (y + 1, x)
    yield (y, x - 1)
    yield (y, x + 1)


def shortest(starts):
    costs = {end: 0}
    q = [(0, end)]

    while q:
        val, current = heapq.heappop(q)
        new_cost = costs[current] + 1
        for n in neighbours(current):
            if n not in heights:
                continue
            if (heights[n] + 1) >= heights[current]:
                if new_cost < costs.get(n, 1000000):
                    costs[n] = new_cost
                    heapq.heappush(q, (new_cost, n))

    return min(costs[x] for x in starts if x in costs)


print(f"Part 1: {shortest({start})}")
print(f"Part 2: {shortest({c for c, h in heights.items() if h == ord('a')})}")
