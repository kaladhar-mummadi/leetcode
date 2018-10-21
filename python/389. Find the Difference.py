class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = {}
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in t:
            if c in letters and letters[c] > 0:
                letters[c] -= 1
            else:
                return c
