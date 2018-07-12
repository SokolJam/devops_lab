def is_leap():
    year = int(input('Input value of year (from 1900 to 100000): '))
    leap = False
    while not 1900 <= year <= 10 ** 5:
        ret = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if ret in 'Yy':
            year = int(input('Input value of year (from 1900 to 100000): '))
        else:
            return 'Exit from script!'
    if not year % 100 and year % 400:
        return leap
    elif year % 4 == 0:
        leap = True
    return leap


print(is_leap())
