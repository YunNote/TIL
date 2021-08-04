a = int(input())

for i in range(1, a + 1):
    print('*' * i , end='')
    print()

for i in range(a-1 , 0, -1):
    print('*' * i, end='')
    print()