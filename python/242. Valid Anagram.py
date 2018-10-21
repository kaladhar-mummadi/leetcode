class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        j = 0
        for ch in s:
            if ch != t[j]:
                return False
            j += 1
        return True

