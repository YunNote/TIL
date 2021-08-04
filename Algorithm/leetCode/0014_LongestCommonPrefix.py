from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minWord = min(strs, key=len)
        prefix = minWord
        check = True
        for i in range(0 , len(minWord)) :
            prefix = prefix[:len(minWord) - i]
            check = True
            for j in strs[:] :
                if j.find(prefix) != 0 :
                    check = False
            if check:
                break

        if check:
            return prefix
        else:
            return ("")

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
    print(Solution().longestCommonPrefix(["reflower","flow","flight"]))

