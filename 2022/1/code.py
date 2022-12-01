# Advent of code Year 2022 Day 1 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input_list = input_file.read()

inputs = input_list.split("\n")
max_value = 0
current_value = 0
for input in inputs:
    if(input != ""):
        current_value += int(input)
    else:
        if(current_value > max_value): 
            max_value = current_value
        current_value = 0

print("Part One : "+ str((max_value)))

max_values = [0, 0, 0]
current_values = 0
for input in inputs:
    if(input != ""):
        current_values += int(input)
    else:
        for i in range(len(max_values)):
            if(current_values > max_values[i]): 
                max_values[i] = current_values
                break
        current_values = 0

print("Part Two : "+ str(sum(max_values)))