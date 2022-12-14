#!/usr/bin/env python3

from itertools import pairwise


def inclusive(a, b):
    return range(a, b + 1) if a < b else range(b, a + 1)


def draw(segments):
    for a, b in pairwise(segments):
        if a[0] == b[0]:
            yield from ((a[0], vy) for vy in inclusive(a[1], b[1]))
        else:
            yield from ((vx, a[1]) for vx in inclusive(a[0], b[0]))


with open("day14-input.txt") as f:
    scan = set()
    for line in f:
        scan.update(draw(tuple(int(n) for n in p.split(','))
                         for p in line.split(" -> ")))


def fall(grain):
    x, y = grain
    yield (x, y + 1)
    yield (x - 1, y + 1)
    yield (x + 1, y + 1)


def pour(scan, floor=False):
    bottom = max(y for x, y in scan)
    occ = set(scan)
    start = (500, 0)
    while start not in occ:
        pos = start
        while True:
            if not floor:
                if pos[1] >= bottom:
                    return len(occ) - len(scan)
            for n in fall(pos):
                if n not in occ and n[1] != bottom + 2:
                    pos = n
                    break
            else:
                break
        occ.add(pos)
    return len(occ) - len(scan)


print(f"Part 1: {pour(scan)}")
print(f"Part 2: {pour(scan, floor=True)}")
