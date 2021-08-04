numbersSet = set(range(10001))
notSelfNumbersSet = set()


for i in range(0, 10001) :
    for j in str(i) :
        i += int(j)
    notSelfNumbersSet.add(i)


selfNumbers = numbersSet - notSelfNumbersSet
for i in sorted(selfNumbers) :
    print(i)