from os import extsep


tab = []
with open("Day3\puzzle_input.txt") as puzzle:
    data = puzzle.readlines()
    for element in data:
        tab.append(element.split("\n")[0])
        
test = [
    '011011',
    '011101',
    '100110',
    '011101'
]
elements = []
gamma = []
epsilon = []
length = len(tab[1])


for i in range(length):
    for element in tab:
        elements.append(element[i])
    if elements.count("1") > elements.count("0"):
        gamma.append("1")
    else:
        gamma.append("0")
    elements.clear()
    
for bits in gamma:
    if bits == "1":
        epsilon.append("0")
    else:
        epsilon.append("1")

print(gamma) 
print(epsilon)
str_gamma = ''.join(str(e) for e in gamma)
str_epsilon = ''.join(str(e) for e in epsilon)

print(str_gamma)
print(str_epsilon)

print(int(str_epsilon, 2) * int(str_gamma, 2))