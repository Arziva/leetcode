class Solution:
    def containsDuplicate(self, nums) -> bool:
        x = {} #dict
        for i in range(len(nums)):
            if nums[i] in x:
                return True
            x[nums[i]] = 0 
        return False
            