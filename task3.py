import sys


# This function is responsible for input from console.
def input_value():
    value = int(input('Input N (0 ≤ N ≤ 10 ** 9): '))
    if (value < 0) or (value > 10 ** 9):
        retry = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if retry in 'Yy':
            return input_value()
        else:
            sys.exit()
    return value


# This function checks would number have divisor at all?
def factor(n):
    i = 2
    array_fact = []
    while i * i <= n:
        while n % i == 0:
            array_fact.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        array_fact.append(int(n))
    return array_fact


# The function checks whether the number is prime?
def simple(x):
    if x > 9:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True

    else:
        return x


# The function calculates minimal natural number.
def natural():
    n = input_value()
    print('N = {}'.format(n))
    for i in factor(n):
        if simple(i) is True:
            return -1

    q = 0
    result = 1
    while result != n:
        result = 1
        q += 1
        for i in str(q):
            result *= int(i)
    return q


print('Minimal Q = {}'.format(natural()))
