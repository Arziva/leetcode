class Solution:
    def twoSum(self, nums, target) ->int:
        prevmap = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in prevmap:
                return [prevmap[remaining], i]
            prevmap[n] = i
        return