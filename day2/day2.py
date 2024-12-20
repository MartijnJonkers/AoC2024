import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

input = [[int(val) for val in str.split(line, " ")] for line in aoc.loadlines()]

# compute valid step between levels (0 = invalid step, 1 = valid rising step, -1 = valid falling step)
step  = [[(1 if (l[i]-l[i+1]) > 0 else -1) if 1 <= abs(l[i]-l[i+1]) <= 3 else 0 for i in range(0, len(l)-1)] for l in input]

# the abs sum of the steps must match the number level steps in each report (1=valid report, 0 invalid report)
part1 = sum([1 if abs(sum(step[i])) == (len(input[i])-1) else 0 for i in range(0, len(input))])

# same as part 1, but retry when failed by removing 1 element one by one. until report succeeds.
part2 = 0
for report in input:                                                                                             # go over all reports
  for i in range(0, len(report)):                                                                                # go over all values in report
    r = report.copy()                                                                                            # copy line
    r.pop(i)                                                                                                     # remove 1 element at index
    step = [(1 if (r[i]-r[i+1]) > 0 else -1) if 1 <= abs(r[i]-r[i+1]) <= 3 else 0 for i in range(0, len(r)-1)]   # determing step validation
    if abs(sum(step)) == (len(r)-1):                                                                             # abs sum of all steps must be same as (nr of r values-1)
      part2 = part2 + 1                                                                                          # valid report
      break                                                                                                      # go to next report

aoc.result(part1, part2)
