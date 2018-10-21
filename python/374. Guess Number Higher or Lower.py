# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    finalNum = 6
    if num > finalNum:
        return 1
    elif num < finalNum:
        return -1
    return 0
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        num = (l + r) // 2
        res = guess(num)
        while res != 0:
            if res < 0:
                r = num - 1
            elif res > 0:
                l = num + 1
            num = (l + r) // 2
            res = guess(num)
        return num
sol = Solution()
print(sol.guessNumber(10))