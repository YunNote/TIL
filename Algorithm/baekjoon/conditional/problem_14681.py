x = int(input()) > 0
y = int(input()) > 0
if x and y:
    print(1)
elif x and not y:
    print(4)
elif not x and not y:
    print(3)
else:
    print(2)
