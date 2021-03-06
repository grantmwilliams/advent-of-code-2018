## Expects Input to exist in file in same folder named "data.txt"
# Part 1
print(sum(map(int,open('data.txt').read().splitlines())))

# part 2
from itertools import cycle, accumulate

s = set([0]) 
print(next(res for res in accumulate(cycle(map(int,open('data.txt').read().splitlines()))) if res in s or s.add(res))
