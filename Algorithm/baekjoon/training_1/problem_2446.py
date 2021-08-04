a = int(input())
size = int(a * 2 / 2)
for i in range(0, size):
    print(' ' * i, end='')
    print('*' * ((a - i) * 2 - 1))

for i in range(size - 2, -1, -1):
    print(' ' * i, end='')
    print('*' * ((a - i) * 2 - 1))
