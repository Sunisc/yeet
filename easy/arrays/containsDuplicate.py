# contains duplicate
# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)

        return False

s = Solution()
s.containsDuplicate([1,2,3,4,4])