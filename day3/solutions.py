#sol for day 3
def find_valid_instructions(x, toggle=False):
    
    uncorrupted = "mul("
    do = "do()"
    dont = "don't()"
    result = 0
    i = 0
    enabled = True
    
    while i < len(x):
        if len(x) - i < len(uncorrupted):
            break
        if x[i:i+4] == uncorrupted:
            i+=4
            int_1 = ""
            while i < len(x) and x[i].isdigit():
                int_1+=x[i]
                i+=1
            if not int_1 or i >= len(x) or x[i] != ",":
                continue
            i+=1
            int_2=""
            while i<len(x) and x[i].isdigit():
                int_2+=x[i]
                i+=1
            if not int_2 or i >= len(x) or x[i] != ")":
                continue
            if enabled:
                result+=int(int_1)*int(int_2)
        elif x[i:i+4] == do and toggle:
            enabled=True
            i+=4
            continue
        elif x[i:i+7] == dont and toggle:
            enabled=False
            i+=7
            continue
        i+=1
    return result
    

with open('input.txt', 'r') as f:
    line = f.read()

part_1 = find_valid_instructions(line)
print("Sol 1:", part_1)
part_2 = find_valid_instructions(line,True)
print("Sol 2:", part_2)