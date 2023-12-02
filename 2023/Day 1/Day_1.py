# THIS IS UNRESOLVED FOR NOW, I WILL TRY TO FIX IT BEFORE DECEMBER 25th

file = open("Day_1_input.txt", "r")

inputs = []

for line in file:
    inputs.append(line)

file.close()

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
digits_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
two_digits_line = ''
total_digits = 0

fixed_inputs = []

for line in inputs:
    replaceable_line = line
    og_text = ''
    for character in line:
        og_text += character
        for digit in digits_text:
            if digit in og_text:
                index = digits_text.index(digit)
                replaceable_text = og_text.replace(digit, digits[index])
                replaceable_line = replaceable_line.replace(og_text, replaceable_text)
                og_text = ''
    fixed_inputs.append(replaceable_line)

for line in fixed_inputs:
    print(line)
    for character in line:
        if character in digits:
            two_digits_line += character
            break
    line_1 = line[::-1]
    print(line_1)
    for character in line_1:
        if character in digits:
            two_digits_line += character
            break
    print(two_digits_line)
    total_digits += int(two_digits_line)
    two_digits_line = ''

print(total_digits)