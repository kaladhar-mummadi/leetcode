class Solution:
    def brute_force(self, haystack, needle):
        hay_stack_len = len(haystack)
        needle_len = len(needle)
        res = -1
        if needle_len == 0:
            return 0
        if needle_len > hay_stack_len:
            return -1
        for i in range(hay_stack_len - needle_len + 1):
            j = 0
            while j < needle_len and (i + j) < hay_stack_len:
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    break

            if j == needle_len:
                res = i
                break

        return res

    # create lps array, longest prefix which is also a suffix
    def create_lps(self, s):
        lps = [0]*len(s)
        j = 0
        i = 1
        while i < len(s):
            if s[i] == s[j]:
                lps[i] = j + 1
                j += 1
            elif j > 0:
                j = lps[j-1]
                i -= 1

            i += 1
        return lps

    def kmp_algo(self, haystack, needle):
        hay_stack_len = len(haystack)
        needle_len = len(needle)
        res = -1
        if needle_len == 0:
            return 0
        if needle_len > hay_stack_len:
            return res

        lps = self.create_lps(needle)
        i = 0
        j = 0
        while i < hay_stack_len:
            if j == needle_len:
                break
            if needle[j] == haystack[i]:
                j += 1
            elif j > 0:
                j = lps[j-1]
                i -= 1


            i += 1

        if j == needle_len:
            res = i - j
            return res
        return -1

    def strStr(self, haystack, needle):
        return self.kmp_algo(haystack, needle)
        # return self.brute_force(haystack, needle)

sol = Solution()
print(sol.strStr("aabaaabaaac", "aabaaac"))