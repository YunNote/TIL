from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        list = self.merge(nums1, nums2)
        list.sort()
        size = len(list)
        mok = size // 2
        if size % 2 == 0:
            return sum(list[mok-1:mok + 1]) / 2

        else:
            return list[mok]


    def merge(self, nums1, nums2):
        list = []
        for x in nums1: list.append(x)
        for x in nums2: list.append(x)

        return list
if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3], [2,7]))
    print(Solution().findMedianSortedArrays([0,0], [0,0]))
    print(Solution().findMedianSortedArrays([1,3], [2]))

