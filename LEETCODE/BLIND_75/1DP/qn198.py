class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0

        #{rob1, rob2, n, n+1, ...}
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

        #for nums = [1,2,3,1]
        #rob1,2 = 0
        #temp = rob1+1 = 1, rob1 = 0, rob2 = 1
        #temp = rob1+2 = 2, rob1 = 1, rob2 = 2
        #temp = rob1+3 = 4, rob1 = 2, rob2 = 4
        #temp = rob1+1 = 3, rob1 = 4, rob2 = 4

        