import math
from collections import Counter


class Solution:
    mod_val = math.pow(10, 9) + 7

    def get_number(self, arr, ind):
        res = 0
        i = arr[0]
        for i in arr:
            if i >= ind:
                break
            res += 1
        return res

    def threeSumMulti(self, A, target):
        i_repeats = {}
        ind = 0
        for i in A:
            if i in i_repeats:
                i_repeats[i].append(ind)
            else:
                i_repeats[i] = [ind]
            ind += 1
        a_len = len(A)
        i = 0
        res = 0
        j = i + 1
        while j < a_len:
            k = j + 1
            while k < a_len:
                temp = A[k]+A[j]
                if i_repeats.get(target-temp):
                    res += self.get_number(i_repeats.get(target-temp), j)
                    res = res % self.mod_val
                k += 1
            j += 1
        return int(res)


sol = Solution()

print(sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
