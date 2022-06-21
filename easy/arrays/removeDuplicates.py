# remove duplicates in sorted array 
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

from collections import OrderedDict
import enum

class Solution:
    # one pointer to keep track of unique and another pointer to skip through dupes
    def removeDuplicates(self, nums: list):
        ocurred = set()
        uniquePointer = 0
        secondPointer = 0

        while secondPointer < len(nums):
            if nums[secondPointer] in ocurred:
                secondPointer += 1
            else:
                nums[uniquePointer] = nums[secondPointer]
                ocurred.add(nums[secondPointer])
                uniquePointer += 1
                secondPointer += 1
        
        return uniquePointer if nums else 0

    # using an ordered list instead of an ordered dict
    def removeDuplicates2(self, nums: list):
        orderedList = []

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                orderedList.append(nums[i])
        
        if nums and not orderedList:
            orderedList.append(nums[0])

        if orderedList[-1] != nums[-1]:
            orderedList.append(nums[-1])
        
        for k,v in enumerate(orderedList):
            nums[k] = v

        return 0 if not nums else len(orderedList)

    # popping is an intensive operation
    def removeDuplicates3(self, nums: list):
        s = set()
        i = 0
        k = len(nums)
        while i < k:
            if nums[i] in s:
                # move the repeated numbers to the end
                nums.append(nums.pop(i))
                k -= 1
            else: 
                s.add(nums[i])
                i += 1 
        return nums, k

s = Solution()
print(s.removeDuplicates([1,1,2,3]))