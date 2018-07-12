a = list(map(int, input('Input first list (separate "<space>"): ').split()))
b = list(map(int, input('Input first list (separate "<space>"): ').split()))
c = []

for i in set(a):
    if i in set(b):
        c.append(i)

print('Result list:', c)
