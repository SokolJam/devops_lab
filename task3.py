import sys


def get_input():
    return int(input('Input N (0 ≤ N ≤ 10 ** 9): '))


def repeat():
    return str(input('Value out of range. Do you wont try again?(y/n) '))


def input_value():
    """The function is responsible for input from console.

    :return: input value

    """
    value = get_input()
    while not 0 <= value <= 10 ** 9:
        retry = repeat()
        if retry in 'Yy':
            value = get_input()
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


if __name__ == '__main__':
    print('Minimal Q =', natural())
