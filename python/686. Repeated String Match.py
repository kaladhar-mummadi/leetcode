class Solution(object):
    def is_substring(self, A,B):

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        S = A
        a_len = len(A)
        b_len = len(B)
        res = 1
        while b_len > len(S):
            S = S+A
            res += 1
        if B in S:
            return res
        S = S+A
        if B in S:
            res += 1
            return res
        return -1
sol = Solution()
print(sol.repeatedStringMatch("abcd", "cdabcdab"))