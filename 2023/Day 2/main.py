file_path = "./2023/Day 2/input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

possible = {
    "red":12,
    "green":13,
    "blue":14
}

res = 0


for line in lines:
    good = True
    red = [1]
    blue = [1]
    green = [1]
    
    line = line.replace("Game ", "")
    new_line = line.split(':')
    num_game = int(new_line[0])
    str_test = new_line[1]
    new_line.pop()
    new_line.append(str_test.split(';'))
    
    for colors in new_line[1]:
        separator_color = colors.split(",")
        print(separator_color)
        
        for color in separator_color:
            if "red" in color:
                red.append(int(color[:3]))
            if "blue" in color:
                blue.append(int(color[:3]))
            if "green" in color:
                green.append(int(color[:3]))
        # for element in red:
        #     if element > possible['red']:
        #         good = False
        # if good:
        #     for element in blue:
        #         if element > possible['blue']:
        #             good = False
        # if good:
        #     for element in green:
        #         if element > possible['green']:
        #             good = False
        
    total_color = max(green) * max(red) * max(blue)
    print(total_color)
        
    if good:
        res += total_color

print(res)
        
   