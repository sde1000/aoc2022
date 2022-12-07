#!/usr/bin/env python3

class Directory:
    def __init__(self, parent):
        self.dirs = {}
        self.filesize = 0
        self.parent = parent

    def size(self):
        return self.filesize + sum(d.size() for d in self.dirs.values())


root = Directory(None)

with open("day07-input.txt") as f:
    cwd = root
    for i in f:
        i = i.strip()
        if i.startswith("$ cd "):
            target = i[5:]
            if target == "/":
                cwd = root
            elif target == "..":
                cwd = cwd.parent
            else:
                cwd = cwd.dirs[target]
        elif i.startswith("$"):
            pass
        else:
            a, b = i.split()
            if a == "dir":
                cwd.dirs[b] = Directory(cwd)
            else:
                cwd.filesize = cwd.filesize + int(a)


def dirs(wd):
    yield wd
    for dir in wd.dirs.values():
        yield from dirs(dir)


print(f"Part 1: {sum(d.size() for d in dirs(root) if d.size() <= 100000)}")
required = root.size() - 40000000
size = min(x for x in sorted(d.size() for d in dirs(root)) if x >= required)
print(f"Part 2: {size}")
