class Solution:
    def reverse(self, x: int) -> int:

        # 2의 31승에 대한 값 저장
        MAX_SIZE = pow(2, 31)

        # x 자체가 0이면 처음부터 0 반환
        if x == 0 : return 0

        # 절대값으로 변경후 문자열 뒤집기
        cx = int(str(abs(x))[::-1])

        if not -MAX_SIZE < cx < MAX_SIZE - 1: return 0
        if x < 0 :
            return -cx
        return cx