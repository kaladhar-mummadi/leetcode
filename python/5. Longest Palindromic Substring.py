class Solution:
    #Time: O(n2) space : O(n2)
    def dp(self, s):
        if len(s) < 2:
            return s
        s_len = len(s)
        isBoolean = [[False for _ in range(s_len)] for _ in range(s_len)]

        left = 0
        right = 0
        # for length 1
        for i in range(s_len):
            isBoolean[i][i] = True
        # for length 2
        for i in range(1,s_len):
            if s[i] == s[i-1]:
                isBoolean[i][i-1] = True

                left = i-1
                right = i
        # for length greater than 3
        for j in range(1, s_len):
            for i in range(j):
                if isBoolean[i+1][j-1] and s[i] == s[j]:
                    isBoolean[i][j] = True
                    if j-i > right-left:
                        right = j
                        left = i
        return s[left:right+1]


    def _expand_around_center(self, s,l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return r-l - 1

    #Time: O(n2) Space: O(1), 2n-1 centers
    def expand_around_center_algo(self,s):
        start = 0
        end = 0
        max_palin_len = 0
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            len1 = self._expand_around_center(s, i, i)
            len2 = self._expand_around_center(s, i, i+1)

            temp_max_len = max(len1, len2)
            if temp_max_len > max_palin_len:
                max_palin_len = temp_max_len
                start = i - (temp_max_len-1)//2
                end = i + (temp_max_len//2)
        return s[start:end+1]


    def longestPalindrome(self, s):

        return self.expand_around_center_algo(s)

