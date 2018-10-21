from collections import Counter


class Solution:
    def fourSumCount(self, A, B, C, D):
        first_sum_list = Counter()
        for a in A:
            for b in B:
                first_sum_list[a+b] += 1

        res = 0
        print(first_sum_list)
        for c in C:
            for d in D:
                temp = c + d
                if first_sum_list.get(-temp):
                    res += first_sum_list[-temp]
        return res


A = [-1, 1, 1, 1, -1]
B = [0, -1, -1, 0, 1]
C = [-1, -1, 1, -1, -1]
D = [0, 1, 0, -1, -1]

sol = Solution()
print(sol.fourSumCount(A, B, C, D))
