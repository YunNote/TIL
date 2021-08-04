class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        i = 0
        total = 0
        romanLength = len(symbols)
        while i <= romanLength:
            if i == romanLength:
                break

            currSymbol = symbols[i]
            index = s.find(currSymbol)

            if index != 0:
                i += 1
                continue
            s = s[index + len(currSymbol):]
            total += values[i]

        return total


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
