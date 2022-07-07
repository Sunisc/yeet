# intersection of two arrays II
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/

from ctypes import pointer
from typing import Dict, List

class Solution:
    # dictionary solution O(N) time + O(N) space
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        def addToList(lesser, more):
            l = []
            d: Dict = {}

            for num in lesser:
                if num in d: d[num] += 1
                else: d[num] = 1

            for num in more:
                if num in d and d[num] != 0:
                    l.append(num)
                    d[num] -= 1
            
            return l

        if len(nums1) < len(nums2):
            return addToList(nums1, nums2)
        else:
            return addToList(nums2, nums1)

    # sorted solution, better if list already sorted. O (N log N + M log M + min(N, M)) time + O (1) space
    def intersect2(self, nums1: List, nums2: List):
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()
        pointerOne = pointerTwo = 0
        l = []

        while pointerOne < len(nums1) and pointerTwo < len(nums2):
            if nums1[pointerOne] < nums2[pointerTwo]:
                pointerOne += 1
            elif nums1[pointerOne] > nums2[pointerTwo]:
                pointerTwo += 1
            else:
                l.append(nums1[pointerOne])
                pointerOne += 1
                pointerTwo += 1

        return l
        

s = Solution()
print(s.intersect2(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))