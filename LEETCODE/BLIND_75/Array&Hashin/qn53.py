#sliding window with O(n)
class Solution:
    def maxSubArray(self, nums) -> int:
        MaxSum=nums[0]
        sumcurr = 0
        for i in nums:
            if sumcurr<0:
                sumcurr = 0
            sumcurr += i
            MaxSum = max(MaxSum, sumcurr)
        return MaxSum
            


