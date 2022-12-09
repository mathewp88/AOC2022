# Advent of code Year 2022 Day 9 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

tail_pos1 = {(0,0)}
tail_pos2 = {(0,0)}
rope1 = [[0,0] for _ in range(2)]
rope2 = [[0,0] for _ in range(10)]

def sign(x):
    return (x > 0) - (x < 0) # True = 1, False = 0

def move_head(head, direction):
    head[0] += 1 if direction == "R" else -1 if direction == "L" else 0
    head[1] += 1 if direction == "U" else -1 if direction == "D" else 0

def move_tail(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        tail[0] += sign(x_diff)
        tail[1] += sign(y_diff)

def move(rope, direction, tail_pos):
    for _ in range(int(direction[1])):
        move_head(rope[0], direction[0])
        for i in range(len(rope) - 1):
            move_tail(rope[i], rope[i+1])
        tail_pos.add(tuple(rope[-1]))

for inputs in input:
    inputs = inputs.split(" ")
    move(rope1, inputs, tail_pos1)
    move(rope2, inputs, tail_pos2)

print("Part One : "+ str(len(tail_pos1)))

print("Part Two : "+ str(len(tail_pos2)))