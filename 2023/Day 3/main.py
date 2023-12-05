file_path = "./2023/Day 3/input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]

result_tab = []
for line in lines:
    result_tab.append(list(line))
    
def complete_digit(main_lines, tab_digit):
    final_digit = []
    row_td = tab_digit[0]
    col_td = tab_digit[1]
    first_digit = main_lines[tab_digit[0]][tab_digit[1]]
    final_digit.append(first_digit)
    
    len_col = len(main_lines[row_td])
    for i in range(col_td-1, -1, -1):
        current_index = main_lines[row_td][i]
        if current_index.isdigit():
            final_digit.insert(0,current_index)
        else:
            break
    
    for j in range(col_td+1, len_col):
        current_index = main_lines[row_td][j]
        if current_index.isdigit():
            final_digit.append(current_index)
        else:
            break
    
    return final_digit
    

def get_digit_arround(main_lines, symbol):
    tab_digit_arround = []
    row_s = symbol[0] - 1
    col_s = symbol[1] - 1
    if symbol[0] < 1:
        row_s = 0
    if symbol[1] < 1:
        col_s = 0
            
    for row in range(row_s, symbol[0]+2):
        for col in range(col_s, symbol[1]+2):
            maybe = main_lines[row][col]
            if maybe.isdigit():
                tab_digit_arround.append([row, col])
    return tab_digit_arround
                
def get_all_symbols(main_lines):
    tab = []
    for elements in main_lines:
        for i in range(len(elements)):
            element = elements[i]
            if element == '*':
                row = main_lines.index(elements)
                col = i
                tab.append([row,col])
    return tab


def remove_duplicate(tab_with_duplicates):
    tab_copy = tab_with_duplicates.copy()
    for i in range(len(tab_with_duplicates)-1):
        element1 = tab_with_duplicates[i]
        element2 = tab_with_duplicates[i+1]
        
        if (element1[0] == element2[0]) and ((element1[1] == element2[1] + 1) or (element1[1] == element2[1] - 1)):
            tab_copy.remove(element1)
    return tab_copy

#return all coordonné * with 2 digit adjacent
# exemple : [[0,1], [0,35], [1,4], [1,23].....]
tab_of_coords_symbols = get_all_symbols(result_tab)
tab_of_coords_digits_arround = []

for element in tab_of_coords_symbols:
    coord_digit_arround = remove_duplicate(get_digit_arround(result_tab, element))
    # return all coordonne of all digit that is arround all the symbol
    #exemple : [ [[0,1], [1,1]], [[1,45], [2,45]] ......]
    tab_of_coords_digits_arround.append(coord_digit_arround)

res = 0
my_digit = []

for coords in tab_of_coords_digits_arround:
    for coord in coords:    
        digit = ''.join(complete_digit(result_tab, coord))
        digit = int(digit)
        my_digit.append(digit)
    for i in range(len(my_digit) -1):
        res += (my_digit[i]*my_digit[i+1])
    my_digit.clear()

print(res)
