#!/usr/bin/env python3

with open("day04-input.txt") as f:
    elves = [[[int(x) for x in a.split('-')] for a in i.split(',')]
             for i in f]

elves = [[frozenset(range(x[0], x[1] + 1)) for x in a] for a in elves]

print(f"Part 1: {sum(a.issubset(b) or b.issubset(a) for a, b in elves)}")
print(f"Part 2: {sum(not a.isdisjoint(b) for a, b in elves)}")
