class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        index = 0
        result = ""
        while num > 0:
            mok = num // values[index]
            num = num % values[index]
            for i in range(0, mok):
                result += symbols[index]
            index += 1
        return result

if __name__ == '__main__':
    print(Solution().intToRoman(994))