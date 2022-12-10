#!/usr/bin/env python3

with open("day10-input.txt") as f:
    program = [(l[:4], int(l[5:]) if len(l) > 5 else None) for l in f]


def run(program):
    X = 1
    for ins, val in program:
        yield X
        if ins == "addx":
            yield X
            X = X + val


part1 = sum(a * b for a, b in enumerate(run(program), start=1)
            if a in (20, 60, 100, 140, 180, 220))

print(f"Part 1: {part1}")

print("Part 2:")
cycles = run(program)
for _ in range(6):
    print(''.join('#' if col in (X - 1, X, X + 1) else '.'
                  for col, X in zip(range(40), cycles)))
