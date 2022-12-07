# Advent of code Year 2022 Day 7 solution
# Author = Mathai Mathew
# Date = December 2022

from tree import Tree

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split("\n")

dir = Tree()

for inputs in input[1:]:
    inputs = inputs.split(" ")
    if inputs[0] == "$":
        folder = inputs[-1]
        if folder == "..":
            dir.up()
        elif folder != "ls":
            dir.add_node(folder)
    else:
        size, name = inputs
        if size != "dir":
            dir.add_node(name, int(size))

dir.update_size()
size = sum(filter(lambda x: x <= 100000, dir.dirs))

print("Part One : "+ str(size))

unused_space = 70000000 - dir.root.size
space_needed = 30000000 - unused_space
dir_to_delete = min(filter(lambda x: x >= space_needed, dir.dirs))

print("Part Two : "+ str(dir_to_delete))