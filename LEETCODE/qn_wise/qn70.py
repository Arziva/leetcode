class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n == 1 or n == 2:
                return n
            else:
                return ( fib(n-1) + fib(n-2))
        return fib(n)