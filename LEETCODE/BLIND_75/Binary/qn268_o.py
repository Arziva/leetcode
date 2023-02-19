class Solution:
    def missingNumber(self, nums) -> int:
        x = {i for i in range(len(nums)+1)}
        for i in nums:
            if i in x:
                x.remove(i)
        return x.pop()
                