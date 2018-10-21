class Solution(object):
    def isMatch(self, s, p):
        rows = len(s) + 1
        columns = len(p) + 1
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, columns):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]

        for i in range(1, rows):
            for j in range(1,columns):
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    temp = dp[i][j - 2]
                    if temp:
                        dp[i][j] = dp[i][j - 2]
                    elif s[i-1] == p[j-2] or p[j-2] == ".":
                        dp[i][j] = dp[i-1][j]

        return dp[rows-1][columns-1]

sol = Solution()
print(sol.isMatch("aa","a*"))
