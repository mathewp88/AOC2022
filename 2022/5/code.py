# Advent of code Year 2022 Day 5 solution
# Author = Mathai Mathew
# Date = December 2022

import copy

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

boxes, moves = input.split("\n\n")
moves = [[int(i) for i in move.split(" ") if i.isdigit()]  for move in moves.split("\n")]
boxes = [row[1::4] for row in boxes.split("\n")[:-1]]
boxes = [[box for box in col[::-1] if box != ' '] for col in zip(*boxes)]
boxes2 = copy.deepcopy(boxes)

for move in moves:
    for i in range(move[0]):
        boxes[move[2]-1].append(boxes[move[1]-1].pop())
ans1 = "".join([str(box[-1]) for box in boxes])

print("Part One : "+ str(ans1))

for move in moves:
        boxes2[move[2]-1] = boxes2[move[2]-1] + boxes2[move[1]-1][-(move[0]):]
        boxes2[move[1]-1] = boxes2[move[1]-1][:-move[0]]
ans2 = "".join([str(box[-1]) for box in boxes2])

print("Part Two : "+ str(ans2))