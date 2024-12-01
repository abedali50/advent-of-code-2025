#sol for day 1
from collections import Counter

def tot_dist(row_l,row_r):
    row_l.sort()
    row_r.sort()
    count=0
    for i in range(len(row_l)):
        count+=abs(row_l[i]-row_r[i])
    return count

def sim_score(row_l,row_r):
    r_count = Counter(row_r)
    sim_score =0
    for i in row_l:
        sim_score+=i*r_count[i]
    return sim_score

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

row_l = []
row_r = []

for line in lines:
    l, r = line.split()
    row_l.append(int(l))
    row_r.append(int(r))
    
tot_dist = tot_dist(row_l,row_r)
print("Sol 1:", tot_dist)

sim_score = sim_score(row_l,row_r)
print("Sol 2:", sim_score)