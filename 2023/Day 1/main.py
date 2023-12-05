import re
file_path = "./2023/Day 1/input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
      ]

both = 0
res = 0
first = 0
last = 0
found = False

for line_default in lines:
    line = line_default
    while(not found):
        for unit in units:
            if line.startswith(unit):
                first = int(units.index(unit))
                found = True
        if line[0].isdigit() and not found:
            first = int(line[0])
            found = True
        else:
            liste_line = list(line)
            liste_line.pop(0)
            line = ''.join(liste_line)
    
    found = False
    line = line_default

    while(not found):
        for unit in units:
            if line.endswith(unit):
                last = int(units.index(unit))
                found = True
        if line[-1].isdigit() and not found:
            last = int(line[-1])
            found = True
        else:
            liste_line = list(line)
            liste_line.pop()
            line = ''.join(liste_line)
    found = False
    
    both = first*10 + last
    res += both

print(res)

