# Advent of code Year 2022 Day 3 solution
# Author = Mathai Mathew
# Date = December 2022

with open(__file__.rstrip("code.py")+"input.txt", 'r') as input_file:
    input = input_file.read()

inputs = input.split("\n")
lines = [[[int(i) for i in j.split("-")] for j in k.split(",")] for k in inputs]

ans1 = sum(a <= c <= d <= b or c <= a <= b <= d for (a,b), (c,d) in lines)
ans2 = sum([max(a,c) <= min(b,d) for (a,b), (c,d) in lines])

print("Part Two : "+ str(ans1))


print("Part Two : "+ str(ans2))