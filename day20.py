#!/usr/bin/env python3

with open("day20-input.txt") as f:
    enc = [int(x) for x in f]


class elem:
    __slots__ = ["val", "move", "prev", "next"]

    def __init__(self, val, move):
        self.val = val
        self.move = move

    def mix(self):
        if self.move == 0:
            return
        self.prev.next = self.next
        self.next.prev = self.prev
        cur = self
        if self.move > 0:
            for _ in range(self.move + 1):
                cur = cur.next
        else:
            for _ in range(-self.move):
                cur = cur.prev
        self.prev = cur.prev
        self.next = cur
        self.prev.next = self
        self.next.prev = self


def mklist(enc, key=1):
    elems = [elem(x * key, (x * key) % (len(enc) - 1)) for x in enc]
    head = None
    for i, e in enumerate(elems):
        e.prev = elems[i - 1]
        e.next = elems[(i + 1) % len(elems)]
        if e.val == 0:
            head = e
    return head, elems


def coords(head):
    cur = head
    v = 0
    for _ in range(3):
        for _ in range(1000):
            cur = cur.next
        v = v + cur.val
    return v


head, elems = mklist(enc)
for e in elems:
    e.mix()
print(f"Part 1: {coords(head)}")

head, elems = mklist(enc, key=811589153)
for _ in range(10):
    for e in elems:
        e.mix()
print(f"Part 2: {coords(head)}")
