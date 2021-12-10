with open("Day2\data.txt") as file:
    data = file.readlines()
 
liste = []
for line in data:
    index = 0
    words = line.split('\n')
    liste.append(words[0])

forward = []
up = []
down = []

add_forward = 0
add_up = 0
add_down = 0

aim = 0
depth = 0

for element in liste:
    direction = element.split(' ')
    if direction[0] == "forward":
        add_forward += int(direction[1])
        depth += int(direction[1]) * aim
    elif direction[0] == "up":
        aim -= int(direction[1])
    else:
        aim += int(direction[1])


# for number_forward in forward:
#     add_forward += int(number_forward)

# for number_up in up:
#     add_up += int(number_up)
    
# for number_down in down:
#     add_down += int(number_down)
    
print(add_forward)
print(depth)
print(aim)
print(add_forward * depth)