# Data Read 
data = open('data.txt').read().splitlines()

# Data Shape
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

# Split Data in Vars
def parse(row):
    num, _, xy, offset = row.split()
    num = num[1:]
    x, y = xy[:-1].split(",")
    w, h = offset.split('x')
    return int(num), int(x), int(y), int(w), int(h)


from collections import defaultdict

# Part 1
overlap = defaultdict(int)
for row in data:
    num, x, y, w, h = parse(row)

    for xi in range(w):
        for yi in range(h):
            overlap[(x+xi, y+yi)] += 1

print(len([v for k,v in overlap.items() if v > 1]))

# Part 2
all_claims = set()
overlap_claims = set()
for row in data:
    num, x, y, w, h = parse(row)

    all_claims.add(num)
    for xi in range(w):
        for yi in range(h):
            xy = (x+xi,y+yi)
            if overlap[xy] > 1:
                overlap_claims.add(num)
            overlap[xy] += 1
print(next(f for f in all_claims-overlap_claims))