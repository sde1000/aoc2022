#!/usr/bin/env python3

from functools import cmp_to_key, reduce
from itertools import zip_longest
from operator import mul
import json

with open("day13-input.txt") as f:
    packets = [json.loads(x) for x in f.read().splitlines() if x]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left > right else -1 if right > left else 0
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    for idx in range(len(left)):
        if idx >= len(right):
            return 1
        if (r := compare(left[idx], right[idx])) != 0:
            return r
    return -1


part1 = sum(idx for idx, pair in enumerate(
    zip_longest(*[iter(packets)] * 2), start=1) if compare(*pair) == -1)
print(f"Part 1: {part1}")

dividers = ([[2]], [[6]])
packets.extend(dividers)
packets.sort(key=cmp_to_key(compare))

print(f"Part 2: {reduce(mul, (packets.index(div) + 1 for div in dividers))}")
