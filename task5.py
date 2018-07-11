value = int(input('Input a positive integer: '))

length = len(bin(value)[2:])
if length <= 32:
    result = value ^ (2 ** length - 1)
    print(result)
