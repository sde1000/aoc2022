#!/usr/bin/env python3

with open("day03-input.txt") as f:
    rucksacks = [x.strip() for x in f.readlines()]


def priority(item):
    return ord(item) - (96 if item.islower() else 38)


def common_priority(rucksack):
    l, r = (rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:])
    for c in l:
        if c in r:
            return priority(c)


def groups(rucksacks):
    r = iter(rucksacks)
    try:
        while True:
            yield (next(r), next(r), next(r))
    except StopIteration:
        return


def badge_item_priority(group):
    for c in group[0]:
        if c in group[1] and c in group[2]:
            return priority(c)


print(f"Part 1: {sum(common_priority(r) for r in rucksacks)}")
print(f"Part 2: {sum(badge_item_priority(g) for g in groups(rucksacks))}")
