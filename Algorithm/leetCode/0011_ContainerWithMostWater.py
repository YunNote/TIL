from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0

        while (right - left) > 0:
            rHeight = height[right]
            lHeight = height[left]

            max_area = max(max_area, ((right - left) * min(rHeight, lHeight)))

            if rHeight <= lHeight:
                right -= 1
            else:
                left += 1

        return max_area


if __name__ == '__main__':

    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
