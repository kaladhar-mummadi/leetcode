class Solution:
    def getPrimeNumbers(self, N):
        prime_number_arr = []
        numbers = [True] * N
        i = 2
        while i * i <= N:
            if numbers[i]:
                j = i * 2
                while j < N:
                    numbers[j] = False
                    j += i
            i += 1
        i = 2
        prev = 0
        j = 0
        res = 0
        while i < N:
            if numbers[i]:
                res += 1
            i += 1
        return res

    def countPrimes(self, n):
        return self.getPrimeNumbers(n)