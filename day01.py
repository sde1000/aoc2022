#!/usr/bin/env python3

with open("day01-input.txt") as f:
    elves = [sum(int(x) for x in e.split("\n") if x)
             for e in f.read().split("\n\n")]

print(f"Part 1: {max(elves)}")
print(f"Part 2: {sum(list(sorted(elves))[-3:])}")
