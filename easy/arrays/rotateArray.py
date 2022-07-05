# rotate array
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/

from audioop import reverse


class Solution:

    # using another list as reference O(n) extra space
    def rotate(self, nums: list, k: int):
        k %= len(nums)
        if not k: return nums

        cln = nums.copy()
        pointerTwo = k

        for pointerOne in range(0, len(nums)):
            nums[pointerTwo] = cln[pointerOne]
            pointerTwo += 1
            pointerTwo %= len(nums)

        return nums
    
    # using array reversal
    def rotate2(self, nums: list, k: int):
        k %= len(nums)
        if not k: return nums
        
        nums = nums[::-1]
        nums = nums[0:k][::-1] + nums[k::][::-1]

        return nums
    
    # using cyclical dependencies. either the array will loop through everything, or repeat itself (so we move it manually)
    # https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
    def rotate3(self, nums: list, k: int):
        k %= len(nums)
        if not k: return nums
        swapCount = 0
        startIndex = 0

        while swapCount < len(nums):
            prevIndex = startIndex
            prevValue = nums[prevIndex]

            while True:
                nextIndex = (prevIndex + k) % len(nums)
                tmp = nums[nextIndex]
                nums[nextIndex] = prevValue
                prevValue = tmp
                prevIndex = nextIndex
                swapCount += 1

                if nextIndex == startIndex:
                    break

            startIndex += 1 

        return nums

s = Solution()
print(s.rotate3([1,2,3,4,5,6,7], 3))