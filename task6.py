import re
import sys


# The function checks total count of numbers and signs.
def number_check(num_ch, sign_ch):
    try:
        if (len(num_ch) < 3) or (len(sign_ch) > 2) or (len(sign_ch) < 1):
            raise ValueError
        for num in num_ch:
            int(str(num))
    except ValueError:
        print('ERROR (This formula is not correct!)')
        sys.exit()


# The function return correct formula's format for checking.
def format_check(num_f, sign_f):
    full_formula = []
    for element in num_f:
        full_formula.append(str(element))
    if len(sign_f) == 1:
        full_formula.insert(2, sign_f[0])
    else:
        full_formula.insert(1, sign_f[0])
        full_formula.insert(3, sign_f[1])
    return ''.join(full_formula)


# The function return result of calculations.
def result(numbers, sign_list):
    if '*' in sign_list:
        return numbers[0] * numbers[1]
    elif '/' in sign_list:
        return numbers[0] / numbers[1]
    else:
        return numbers[0] + numbers[1]


formula = input('Input a formula: ')
signs = []
values = []

# Checking that input string does not contain letters and spaces.
if (re.search(r'[ a-zA-Z]', formula)) is not None:
    print('ERROR (This formula is not correct!)')
    sys.exit()

# Selection values from string.
number = re.split(r'\W', formula)
for i in number:
    if i != '':
        values.append(int(i))

# Checking, the value is positive or negative.
skip = 0
for pos, item in enumerate(values):
    index = formula.find(str(item), skip)
    skip = index + 1
    if formula[index-1] == '-':
        values[pos] = -item

# Selection signs of mathematical operations from string.
for sign in formula:
    if sign in r'+*/=':
        signs.append(sign)

number_check(values, signs)
if formula != format_check(values, signs):
    print('ERROR (This formula is not correct!)')
    sys.exit()

if values[2] == result(values, signs):
    print('YES (Everything "OK". Your score is "5"!)')
else:
    print('NO (The calculations are FALSE. Your score is "2"!)')
