## Input data still assumed to be in "data.txt"
# Part 1
from collections import Counter
a, b = 0, 0
for w in open('data.txt').read().splitlines():
    counts = Counter(Counter(w).values())
    if 2 in counts:
        a+=1
    if 3 in counts:
        b+=1

print(a*b)

#Part 2
data = open('data.txt').read().splitlines()
for x in data:
    for y in data:
        diff = [i for i,j in zip(x,y) if i == j]
        if len(y)-len(diff) == 1:
            print("".join(diff))
            break