from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        size = len(nums)
        for i in range(0, size):
            if i == (size - 1): break
            for j in range(i + 1, size):
                total = nums[i] + nums[j]
                if (total == target) is True:
                    return [i, j]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
