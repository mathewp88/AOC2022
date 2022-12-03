# Advent of code Year 2022 Day 2 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

inputs = input.split("\n")

points = 0

pointPerChoice = {"X": 1, "Y": 2, "Z": 3}

choices = { "X":  {"weakTo": "B", "strongTo": "C"},
            "Y":  {"weakTo": "C", "strongTo": "A"},
            "Z":  {"weakTo": "A", "strongTo": "B"}
            }

for round in inputs:
    choice = round.split()
    if(choices[choice[1]]["strongTo"] == choice[0]):
        points += 6
    elif(choices[choice[1]]["weakTo"] != choice[0]):
        points += 3
    points += pointPerChoice[choice[1]]

print("Part One : "+ str(points))

points = 0

pointsPerOutcome = {"X": 0, "Y": 3, "Z": 6}
choices = { "A":  {"X": 3, "Y": 1, "Z": 2},
            "B":  {"X": 1, "Y": 2, "Z": 3},
            "C":  {"X": 2, "Y": 3, "Z": 1}
            }

for round in inputs:
    choice = round.split()
    points += pointsPerOutcome[choice[1]]
    points += choices[choice[0]][choice[1]]

print("Part Two : "+ str(points))