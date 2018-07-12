from collections import defaultdict
import sys

group_a = []
group_b = []
def_dict = defaultdict(list)


def input_array():
    """
    The function is responsible for input from console first pair of integers.

    :return: array which include count of elements in group A and B

    """

    integers = [int(x) for x in input('Input list (separate " "): ').split()]
    while len(integers) < 2 or not 0 <= integers[0] <= 10000 \
            or not 0 <= integers[1] <= 100:
        ret = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if ret in 'Yy':
            integers = [int(x) for x in input('Input list '
                                              '(separate " "): ').split()]
        else:
            print('Exit from script!')
            sys.exit()
    print('Integers =', integers)
    return integers


def input_word(count, group):
    """
    The function is responsible for input from console elements of groups.

    :param count: count of words
    :param group: group's name
    :return:
    """

    word = input('Enter %s word for group "%s": ' % (count, group))
    if not 1 <= len(word) < 100:
        ret = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if ret in 'Yy':
            word = input('Enter %s word for group "%s": ' % (count, group))
        else:
            print('Exit from script!')
            sys.exit()
    return word


integers_array = input_array()
for n in range(integers_array[0]):
    group_a.append(input_word(n + 1, 'A'))

for m in range(integers_array[1]):
    group_b.append(input_word(m + 1, 'B'))

for i in group_b:
    if i in group_a:
        for index, j in enumerate(group_a):
            if i == j:
                def_dict[i].append(index + 1)
    else:
        def_dict[i].append(-1)


print('Group A:', group_a)
print('Group B:', group_b)

for i in def_dict.keys():
    print('Element "%s" locate on the side: %s' % (i, def_dict[i]))
