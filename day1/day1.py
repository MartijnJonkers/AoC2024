import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

# array of 1000 rows with each 2 elements
input = [[int(val) for val in str.split(line, "   ")] for line in aoc.loadlines()]

# rotate array to get 2 rows with each 1000 elements
rotated = list(zip(*input))

# part 1 : sort each row and sum each column difference
sorted = [sorted(column) for column in rotated]
part1 = sum([abs(sorted[0][i] - sorted[1][i]) for i in range(0, len(sorted[0]))])

# part 2 : count each nr of occurances in second row for each value in first row
part2 = sum([(x * rotated[1].count(x)) for x in rotated[0]])

# print result
aoc.result(part1, part2)
