class Solution:
    def missingNumber(self, nums) -> int:
        sum = 0
        sum1 = 0
        for i in range(len(nums)+1):
            sum += i
        for i in nums:
            sum1 += i
        return sum - sum1