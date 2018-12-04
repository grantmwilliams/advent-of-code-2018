import re
from collections import Counter, defaultdict

def parse(line):
    line = line.split(" ")
    dt = tuple(map(int, line[1][:-1].split(":")))
    
    action = re.findall("\d+|wakes|asleep", " ".join(line[2:]))[0]

    return dt, action # ((minute, second), action)

# Data Read 
data = sorted(open('data.txt').read().splitlines())

guards = defaultdict(Counter)
for line in data:
    time, action = parse(line)
    minutes, seconds = time # guess we never needed minutes
    if action != "asleep" and action != "wakes":
        guard = int(action)
    if action == "asleep":
        start = seconds
    if action == "wakes":
        end = seconds
        guards[guard].update(Counter(range(start, end)))
    
# Part 1
ID = max((sum(time.values()), ID) for ID, time in guards.items())[1]
print(ID * guards[ID].most_common()[0][0])

# Part 2
time, ID = max((time.most_common()[0][::-1], ID) for ID, time in guards.items())
print(ID * time[1])