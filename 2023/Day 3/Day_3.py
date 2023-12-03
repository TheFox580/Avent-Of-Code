# THIS IS UNRESOLVED FOR NOW, I WILL TRY TO FIX IT BEFORE DECEMBER 25th


file = open("Day_3_input.txt", "r")

fileinput = []

for line in file:
    line_list = []
    for character in line:
        line_list.append(character)
    fileinput.append(line_list)

file.close()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
not_symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '\n']

"""
check for a symbol in an adjacent spot of a number
"""

sum_part_number = 0

for i in range(len(fileinput)):
    number = ''
    is_a_part_number = False
    for j in range(len(fileinput[i])):
        if fileinput[i][j] in digits:
            number += fileinput[i][j]
            if not is_a_part_number:
                if i != 0 and i != len(fileinput)-1:
                    if j != 0 and j != len(fileinput[i])-1:
                        if fileinput[i-1][j-1] not in not_symbol or fileinput[i-1][j] not in not_symbol or fileinput[i-1][j+1] not in not_symbol or fileinput[i][j-1] not in not_symbol or fileinput[i][j+1] not in not_symbol or fileinput[i+1][j-1] not in not_symbol or fileinput[i+1][j] not in not_symbol or fileinput[i+1][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == 0:
                        if fileinput[i-1][j] not in not_symbol or fileinput[i-1][j+1] not in not_symbol or fileinput[i][j+1] not in not_symbol or fileinput[i+1][j] not in not_symbol or fileinput[i+1][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == len(fileinput[i])-1:
                        if fileinput[i-1][j-1] not in not_symbol or fileinput[i-1][j] not in not_symbol or fileinput[i][j-1] not in not_symbol or fileinput[i+1][j-1] not in not_symbol or fileinput[i+1][j] not in not_symbol:
                            is_a_part_number = True
                elif i == 0:
                    if j != 0 and j != len(fileinput[i])-1:
                        if fileinput[i][j-1] not in not_symbol or fileinput[i][j+1] not in not_symbol or fileinput[i+1][j-1] not in not_symbol or fileinput[i+1][j] not in not_symbol or fileinput[i+1][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == 0:
                        if fileinput[i][j+1] not in not_symbol or fileinput[i+1][j] not in not_symbol or fileinput[i+1][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == len(fileinput[i])-1:
                        if fileinput[i][j-1] not in not_symbol or fileinput[i+1][j] not in not_symbol or fileinput[i+1][j-1] not in not_symbol:
                            is_a_part_number = True
                elif i == len(fileinput)-1:
                    if j != 0 and j != len(fileinput[i])-1:
                        if fileinput[i-1][j-1] not in not_symbol or fileinput[i-1][j] not in not_symbol or fileinput[i-1][j+1] not in not_symbol or fileinput[i][j-1] not in not_symbol or fileinput[i][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == 0:
                        if fileinput[i-1][j] not in not_symbol or fileinput[i-1][j+1] not in not_symbol or fileinput[i][j+1] not in not_symbol:
                            is_a_part_number = True
                    elif j == len(fileinput[i])-1:
                        if fileinput[i-1][j-1] not in not_symbol or fileinput[i-1][j] not in not_symbol or fileinput[i][j-1] not in not_symbol:
                            is_a_part_number = True
        elif fileinput[i][j] not in digits:
            if number != '':
                if is_a_part_number:
                    print(number)
                    sum_part_number += int(number)
                is_a_part_number = False
                number = ''

print(sum_part_number)
