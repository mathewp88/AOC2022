# Advent of code Year 2022 Day 6 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def markers(size):
    marker = 0
    for i in range(len(input) - size):
        if len(set(input[i:i+size])) == size:
            marker = i
            break
    return marker + size


print("Part One : "+ str(markers(4)))



print("Part Two : "+ str(markers(14)))