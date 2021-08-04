for _ in range(int(input())) :
    sum = 0
    count = 1
    ox = input()
    for i in range(len(ox)) :
        if ox[i] == 'O' :
            sum += count
            count +=1
        else:
            count = 1
    print(sum)
