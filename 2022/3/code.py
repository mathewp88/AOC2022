# Advent of code Year 2022 Day 3 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

inputs = input.split("\n")
points = 0
for sack in inputs:
    compartment = [sack[:len(sack)//2], sack[len(sack)//2:]]
    unique = [w for w in set(compartment[0]) if w in set(compartment[1])]
    points += ord(unique[0])- ord('a' if unique[0].islower() else 'A') + (1 if unique[0].islower() else 27)

print("Part One : "+ str(points))

priority = 0
for group in range(len(inputs)//3):
    rucksack = [inputs[group*3], inputs[group*3+1], inputs[group*3+2]]
    badge = [w for w in set(rucksack[0]) if w in set(rucksack[1]) and w in set(rucksack[2])]
    priority += ord(badge[0])- ord('a' if badge[0].islower() else 'A') + (1 if badge[0].islower() else 27)

print("Part Two : "+ str(priority))