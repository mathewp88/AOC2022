# Advent of code Year 2022 Day 10 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

X = 1
cycles = 0
total = 0
screen = ""
addx = False
i = 0

while i < len(input):
    line = input[i].split(" ")
    cycles += 1
    if cycles in [20, 60, 100, 140, 180, 220]:
        total += cycles * X
    if abs(X - ((cycles-1) % 40)) <= 1:
        screen += '#'
    else:
        screen += ' '
    if (cycles % 40) == 0:
        screen += '\n'

    if line[0].strip() == "noop":
        i += 1
    else:
        if addx:
            X += int(line[-1])
            i += 1
            addx = False
        else:
            addx = True

print("Part One : "+ str(total))

print(screen)