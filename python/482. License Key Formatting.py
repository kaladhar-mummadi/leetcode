class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = list(S)
        i = 0
        len_chars = 0
        while i < len(S):
            if S[i] != "-":
                len_chars += 1
            i += 1

        mod_val = len_chars % K
        num_dashes_needed = len_chars // K
        tot_str_len = len_chars + num_dashes_needed + mod_val
        while len(S) < tot_str_len:
            S.append("-")

        return "".join(S)
sol = Solution()
print(sol.licenseKeyFormatting("abcd", 1))