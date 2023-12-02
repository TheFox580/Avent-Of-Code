file = open("Day_2_input.txt", "r")

inputs = []

for line in file:
    inputs.append(line)

file.close()

# Removes the "Game" at the start
for line in inputs:
    if line is not inputs[-1]:
        inputs[inputs.index(line)] = line[:-1]
        inputs[inputs.index(line[:-1])] = line[5:]
    else:
        inputs[inputs.index(line)] = line[5:]

valid_games = []

colors = ["blue", "green", "red"]
max_balls_colors = [14, 13, 12]

max_balls_per_game_power = []
# Check if games are valid or not

for line in inputs:
    is_usable = True
    usable_line = line[3:]
    color_check = ''
    number_of_balls_check = 0
    max_red = 0
    max_blue = 0
    max_green = 0
    for character in usable_line:
        if character != ',' and character != ' ' and character != ';' and character != ':':
            color_check += character
        for color in colors:
            if color in color_check:
                if color == "red":
                    color_check = color_check[:-3]
                    if int(color_check) > max_red:
                        max_red = int(color_check)
                elif color == "blue":
                    color_check = color_check[:-4]
                    if int(color_check) > max_blue:
                        max_blue = int(color_check)
                elif color == "green":
                    color_check = color_check[:-5]
                    if int(color_check) > max_green:
                        max_green = int(color_check)
                number_of_balls_check += int(color_check)
                if number_of_balls_check <= max_balls_colors[colors.index(color)]:
                    color_check = ''
                    number_of_balls_check = 0
                else:
                    is_usable = False
                    color_check = ''
                    break
    if is_usable:
        valid_games.append(line)

    max_balls_per_game_power.append(max_red*max_blue*max_green)

# checking for the ID
ID_add = 0
for line in valid_games:
    ID_Game = ''
    for character in line:
        if character != ':':
            ID_Game += character
        else:
            ID_add += int(ID_Game)
print("Sum of IDs = " + str(ID_add))

# adding powers together
sum_power = 0
for power in max_balls_per_game_power:
    sum_power += power

print("Sum of power = " + str(sum_power))