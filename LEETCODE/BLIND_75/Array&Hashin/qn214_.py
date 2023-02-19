class Solution:
    def containsDuplicate(self, nums) -> bool:
        x = set()
        for i in range(len(nums)):
            if nums[i] in x:
                return True
            x.add(nums[i])
            
        return False
            