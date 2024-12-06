import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc
import re

input = aoc.read()                                                       # read content as string
input = input.replace("mul(", "!)mul(")                                  # make sure invalid mul ends with `)` and does not make a valid mul
results = [0,0]                                                          # init results
for part in [0,1]:                                                       # twice for part1 and part 2:
  if part == 1:                                                           # only for part 2:
    input = [ part.split("don't()")[0] for part in input.split("do()") ]   # split on `do()` and get until `don't()` for each substring
  muls = re.findall(r"mul\((.*?)\)", "".join(input))                      # join all parts and find content between `mul(` and `)`
  muls = [mul.split(",") for mul in muls]                                 # split content on comma
  for mul in muls:                                                        # go over all found muls:
    if(len(mul) == 2 and mul[0].isdigit() and mul[1].isdigit()):           # validate mul parameters:
      results[part] = results[part] + (int(mul[0]) * int(mul[1]))           # sum of muls

aoc.result(results[0], results[1])                                       # print result
