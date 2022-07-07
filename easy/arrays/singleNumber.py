# single number
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: list) -> int:
        if len(nums) == 1: return nums[0]
        output = nums[0]
        
        for i in range(1, len(nums)):
            output ^= nums[i]
        
        return output
        
s = Solution()
print(s.singleNumber([2, 2, 1]))