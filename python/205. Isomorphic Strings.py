class Solution:
    def isIsomorphic(self, s, t):
        chars_s = {}
        chars_t = {}
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        i = 0
        while i in range(s_len):
            chars_s[s[i]] = t[i]
            chars_t[t[i]] = s[i]

            i += 1
        new_str_t = ""
        new_str_s = ""
        i = 0
        while i in range(s_len):
            new_str_t += chars_s[s[i]]
            new_str_s += chars_t[t[i]]
            i += 1
        if new_str_t == t and new_str_s == s:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
