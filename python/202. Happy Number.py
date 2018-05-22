import math


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already_visited = [n]
        while (True):
            res = 0
            if (n == 1):
                return True

            while (n != 0):
                res += math.pow(n % 10, 2)
                n = n // 10
            n = res
            if (n in already_visited):
                return False
            already_visited.append(n)

