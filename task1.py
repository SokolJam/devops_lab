def is_leap():
    year = int(input('Input value of year (from 1900 to 100000): '))
    leap = False
    if 1900 <= year <= 10 ** 5:
        if (year % 100 == 0) and (year % 400 != 0):
            return leap
        elif year % 4 == 0:
            return True
    else:
        retry = str(input('Value out of range.\nDo you wont try again? (y/n)'))
        if retry in 'Yy':
            return is_leap()
    return leap


print(is_leap())
