bugger = 2000
drink = 2000

for i in range(0, 3) :
    a = int(input())

    bugger = min(bugger,a);

for i in range(0, 2):
    a = int(input())
    drink = min(drink, a)

print(bugger + drink - 50)
