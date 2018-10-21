class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = []
        fib.append(0)
        fib.append(1)
        fib.append(2)
        if n < 3:
            return fib[n]
        i = 3
        while i <= n:
            fib.append(fib[i-1] + fib[i-2])
            i += 1
        return fib[n]
sol = Solution()
print(sol.climbStairs(5))