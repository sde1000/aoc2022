#!/usr/bin/env python3

with open("day02-input.txt") as f:
    rounds = [tuple(i.strip().split()) for i in f]

scores = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}

outcome = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
}

print(f"Part 1: {sum(scores[r] for r in rounds)}")
print(f"Part 2: {sum(scores[(r[0], outcome[r])] for r in rounds)}")
