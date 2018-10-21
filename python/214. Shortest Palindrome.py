class Solution(object):
    def brute_force(self, s):
        n = len(s)
        if n == 0:
            return ""
        rev_s = s[::-1]

        for i in range(len(s)):
            if s[0:n - i] == rev_s[i:]:
                return rev_s[:i] + s

    def rec_algo_(self, s):
        i = 0
        if len(s) == 0:
            return ""
        j = len(s) - 1
        while j >= 0:
            if s[i] == s[j]:
                i += 1
            j -= 1

        if i == len(s):
            return s
        rev_s = s[:i-1:-1]
        return rev_s + self.rec_algo_(s[:i]) + s[i:]



    def shortestPalindrome(self, s):
        return  self.rec_algo_(s)
        # return self.brute_force(s)

sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))


