import sys


def input_value():
    """The function is responsible for input from console.
    (with the compliance check)

    :return: input value

    """
    value = int(input('Input N (0 ≤ N ≤ 10 ** 9): '))
    while not 0 <= value <= 10 ** 9:
        retry = str(input('Value out of range. Do you wont try again?(y/n) '))
        if retry in 'Yy':
            value = int(input('Input N (0 ≤ N ≤ 10 ** 9): '))
        else:
            print('Exit from script!')
            sys.exit()
    return value


def factor(n):
    """The function checks would number have divisor at all.

    :param n: checking number
    :return: array of divisors

    """
    i = 2
    array_fact = []
    while i * i <= n:
        while not n % i:
            array_fact.append(i)
            n = n / i
        i += 1
    if n > 1:
        array_fact.append(int(n))
    return array_fact


def simple(x):
    """The function checks whether the number is prime.

    :param x: number
    :return: True if number is prime, False - if not, or number if x <= 9

    """
    if x > 9:
        for i in range(2, x):
            if not x % i:
                return False
        else:
            return True
    else:
        return x


def natural():
    """The function calculates minimal natural number.

    :return: minimal number

    """
    n = input_value()
    print('N =', n)
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


print('Minimal Q =', natural())
