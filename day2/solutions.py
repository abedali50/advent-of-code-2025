#sol for day 2
def all_inc_or_dec(line):
    inc, dec = sorted(line), sorted(line,reverse=True)
    return line in (inc,dec)

def acceptable_diff(line):
    acc = [1,2,3]
    for i in range(1,len(line)):
        diff = abs((line[i-1])-(line[i]))
        if diff not in acc:
            return False
    return True

def safe(line):
    return all_inc_or_dec(line) and acceptable_diff(line)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    
#lines = ['7 6 4 2 1',
#'1 2 7 8 9',
#'9 7 6 2 1',
#'1 3 2 4 5',
#'8 6 4 4 1',
#'1 3 6 7 9']

safe_counter = 0
prob_damp_counter = 0
for line in lines:
    line=line.split(" ")
    line = [int(l) for l in line]
    if safe(line):
        safe_counter+=1
    prob_damp = any([safe(line[:i]+line[i+1:]) for i in range(len(line))])
    if prob_damp:
        prob_damp_counter+=1
        
print("Sol 1:", safe_counter)
print("Sol 2:", prob_damp_counter)
