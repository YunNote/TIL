class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        max = 1

        for i in range(0, size) :
            curr = s[i]

            if i == (size-1): break

            for j in range(i+1, size):
                if curr.find(s[j]) > -1 :
                    break;

                curr = curr + s[j]
                if len(curr) > max:
                    max = len(curr)
        return max



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("pwwkew"))