#!/usr/bin/env python3

import re

movere = re.compile(r'^move (\d+) from (\d+) to (\d+)$')

with open("day05-input.txt") as f:
    stacklines, movelines = (x.splitlines() for x in f.read().split("\n\n"))

width = max(len(x) for x in stacklines)
stacklines = [x + ' ' * (width - len(x)) for x in stacklines]
stacks = [''.join(c for c in s[1:] if c != ' ')
          for s in zip(*reversed(stacklines)) if s[0] != ' ']
moves = [tuple(int(x) for x in movere.match(i).groups()) for i in movelines]


def part1(moves):
    for rep, a, b in moves:
        for _ in range(rep):
            yield (1, a, b)


def rearrange(stacks, moves):
    s = [list(stack) for stack in stacks]
    for depth, a, b in moves:
        c = s[a - 1][-depth:]
        s[a - 1] = s[a - 1][:-depth]
        s[b - 1].extend(c)

    return ''.join(stack[-1] for stack in s)


print(f"Part 1: {rearrange(stacks, part1(moves))}")
print(f"Part 2: {rearrange(stacks, moves)}")
