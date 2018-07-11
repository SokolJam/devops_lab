from collections import defaultdict
import sys

group_a = []
group_b = []
def_dict = defaultdict(list)


# This function is responsible for input from console first pair of integers.
def input_array():
    integers = [int(x) for x in input('Input list (separate " "): ').split()]
    if len(integers) < 2 or (integers[0] < 1) or (integers[1] < 1)\
            or (integers[0] > 10000) or (integers[1] > 100):
        retry = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if retry in 'Yy':
            return input_array()
        else:
            sys.exit()
    print('Integers={}'.format(integers))
    return integers


# This function is responsible for input from console elements of groups.
def input_word(word, group):
    word = input('Enter {i} word for group "{n}": '.format(i=word, n=group))
    if (len(word) < 1) or (len(word) > 100):
        retry = str(input('Value out of range.\nDo you wont try again?(y/n) '))
        if retry in 'Yy':
            input_word(word, group)
        else:
            sys.exit()
    return word


integers_array = input_array()
for n in range(integers_array[0]):
    group_a.append(input_word(n+1, 'A'))

for m in range(integers_array[1]):
    group_b.append(input_word(m+1, 'B'))

for i in group_b:
    if i in group_a:
        for index, j in enumerate(group_a):
            if i == j:
                def_dict[i].append(index + 1)
    else:
        def_dict[i].append(-1)


print('Group A: {a}'.format(a=group_a))
print('Group B: {b}'.format(b=group_b))

for i in def_dict.keys():
    print('Element "{e}" locate on the side: {p}'.format(e=i, p=def_dict[i]))
