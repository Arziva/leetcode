class Solution:
    def maxProduct(self, nums) -> int:

        maxProduct = max(nums)
        curMax, curMin = 1, 1
        for i in nums:
            if i == 0:
                curMax, curMin = 1, 1
            temp = curMax
            curMax = max(i, curMax * i, curMin * i)
            curMin = min(i, temp * i, curMin * i)
            maxProduct = max(maxProduct, curMax)
        return maxProduct