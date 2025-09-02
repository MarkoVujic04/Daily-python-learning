class Solution:
    def singleNumber(self, nums):
        index = 0
        for num in nums:
            index ^= num
        return index

sol = Solution()
print(sol.singleNumber([2, 2, 1]))

