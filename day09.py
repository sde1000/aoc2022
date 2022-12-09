#!/usr/bin/env python3

with open("day09-input.txt") as f:
    moves = [(x[0], int(x[2:])) for x in f]

d = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (1, 0),
    'D': (-1, 0),
}

start = (0, 0)


def expand(moves):
    for direction, count in moves:
        for _ in range(count):
            yield d[direction]


def simulate(moves, knots):
    rope = [list(start) for _ in range(knots)]
    trail = {start}
    for vector in expand(moves):
        cur = rope[0]
        for c in range(2):
            cur[c] = cur[c] + vector[c]
        for knot in range(1, knots):
            prev = cur
            cur = rope[knot]
            if any(abs(prev[c] - cur[c]) > 1 for c in range(2)):
                for c in range(2):
                    if prev[c] > cur[c]:
                        cur[c] = cur[c] + 1
                    elif prev[c] < cur[c]:
                        cur[c] = cur[c] - 1
        trail.add(tuple(rope[-1]))
    return len(trail)


print(f"Part 1: {simulate(moves, knots=2)}")
print(f"Part 2: {simulate(moves, knots=10)}")
