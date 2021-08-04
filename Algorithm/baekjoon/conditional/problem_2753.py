# 윤년이면 1 아니면 0을 출력
# 윤년은 4의 배수이면서 100의 배수가 아닐때 or 400의 배수일때 윤년
year = int(input())
print(((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and 1 or 0)


