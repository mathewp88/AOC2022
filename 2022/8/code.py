# Advent of code Year 2022 Day 8 solution
# Author = Mathai Mathew
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

forest1 = [[int(x) for x in row.strip()] for row in input]
forest2 = list(zip(*forest1))

visible = 0
for i in range(len(forest1)):
    for j in range(len(forest2)):
        tree = forest1[i][j]
        if all(x < tree for x in forest1[i][0:j]) or \
            all(x < tree for x in forest1[i][j+1:]) or \
            all(x < tree for x in forest2[j][0:i]) or \
            all(x < tree for x in forest2[j][i+1:]):
            visible += 1

print("Part One : "+ str(visible))

def get_score(tree, trees):
    score = 0
    for t in trees:
        score += 1
        if t >= tree:
            break
    return score

score = 0
for i in range(len(forest1)):
    for j in range(len(forest2)):
        tree = forest1[i][j]
        s1 = get_score(tree, forest1[i][0:j][::-1])
        s2 = get_score(tree, forest1[i][j+1:])
        s3 = get_score(tree, forest2[j][0:i][::-1])
        s4 = get_score(tree, forest2[j][i+1:])
        temp_score = s1 * s2 * s3 * s4
        score = max(score, temp_score)

print("Part Two : "+ str(score))