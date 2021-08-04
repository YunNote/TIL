## 행의 번호를 기준으로 작업후 join을통해 문자열로 펼침

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        strDict = dict()
        UP = -1
        DOWN = 1
        zigzag = DOWN
        index = 0

        for i in range(0, len(s)):
            if index == numRows -1 :
                zigzag =  UP
            elif index == 0:
                zigzag = DOWN

            v = strDict.get(index, '')
            strDict[index] = v + s[i]
            index += zigzag

        return "".join(strDict.values())
