import math

class Solution(object):
    def getPrimeFactors(self, num):
        res = []
        while num % 2 == 0:
            res.append(2)
            num = num // 2
        i = 3
        while i <= math.sqrt(num):
            while num % i == 0:
                res.append(i)
                num = num // i
            i += 2

        if num > 2:
            res.append(num)
        return res

    def isUgly(self, num):
        if num <= 0:
            return False
        res = self.getPrimeFactors(num)
        # print(res)
        res = list(set(res))
        for i in res:
            if i not in [2, 3, 5]:
                return False
        return True