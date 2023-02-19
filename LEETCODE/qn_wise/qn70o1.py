#fib or climbing stairs 

class Solution:
    def climbStairs(self, n: int) -> int:
        temp = 0
        first = 1
        second = 1
        for i in range(1, n):
            temp = second
            second = first + second
            first = temp
        return second

from qn70o1 import Solution

theclass = Solution()
x = theclass.climbStairs(3)
print(x)