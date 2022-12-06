#!/usr/bin/env python3

with open("day06-input.txt") as f:
    signal = f.readline().strip()


def find_marker(signal, dc):
    for i in range(len(signal) - dc):
        if len(frozenset(signal[i : i + dc])) == dc:
            return i + dc


print(f"Part 1: {find_marker(signal, 4)}")
print(f"Part 2: {find_marker(signal, 14)}")
