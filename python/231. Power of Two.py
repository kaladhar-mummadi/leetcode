class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while (n):
            if (n & 1):
                count += 1
            n = n >> 1
        return  count
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n < 0):
            return False
        no_of_1s = self.hammingWeight(n)
        if no_of_1s == 1:
            return True
        return False