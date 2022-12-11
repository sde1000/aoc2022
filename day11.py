#!/usr/bin/env python3

import operator
import math
from functools import reduce

operators = {
    '*': operator.mul,
    '+': operator.add,
}


class Monkey:
    def __init__(self, lines):
        self.init_items = [int(i) for i in lines[1][18:].split(', ')]
        operator = operators[lines[2][23]]
        try:
            val = int(lines[2][25:])
            self.operation = lambda old: operator(old, val)
        except Exception:
            self.operation = lambda old: operator(old, old)
        self.test = int(lines[3][21:])
        self.dest = (int(lines[5][30:]), int(lines[4][29:]))

    def reset(self):
        self.items = list(self.init_items)
        self.inspectcount = 0

    def turn(self, lcm=None):
        while self.items:
            worry = self.items.pop(0)
            worry = self.operation(worry)
            self.inspectcount = self.inspectcount + 1
            worry = worry % lcm if lcm else worry // 3
            monkeys[self.dest[worry % self.test == 0]].items.append(worry)


with open("day11-input.txt") as f:
    monkeys = [Monkey(s.splitlines()) for s in f.read().split('\n\n')]


# Part 1
for monkey in monkeys:
    monkey.reset()
for round in range(20):
    for monkey in monkeys:
        monkey.turn()

active = sorted(monkey.inspectcount for monkey in monkeys)
print(f"Part 1: {active[-1] * active[-2]}")


# Part 2
def lcm(*n):
    return reduce(lambda x, y: (x * y) // math.gcd(x, y), n)


test_lcm = lcm(*(monkey.test for monkey in monkeys))

for monkey in monkeys:
    monkey.reset()
for round in range(10000):
    for monkey in monkeys:
        monkey.turn(lcm=test_lcm)
active = sorted(monkey.inspectcount for monkey in monkeys)
print(f"Part 2: {active[-1] * active[-2]}")
