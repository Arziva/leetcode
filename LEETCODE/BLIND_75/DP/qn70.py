class Solution:
    def climbStairs(self, n) -> int:
        first = 1
        second = 1
        for i in range(1,n):
            temp = second
            second = first + second
            first = temp
        return second

            