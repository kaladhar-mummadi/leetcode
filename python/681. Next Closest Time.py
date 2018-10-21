class Solution:
    def get_next(self, current, accepted_range, arr):
        i = 0
        next_num = arr[0]
        while i < len(arr):
            if accepted_range[0] <= arr[i] and arr[i] <= accepted_range[-1]:
                if current < arr[i]:
                    next_num = arr[i]
                    return (next_num, False)
            i += 1
        return (next_num, True)
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h1 = [0,1,2]
        h2m2 = list(range(10))
        m1 = list(range(6))
        time_numbers = []
        ranges = [h1,h2m2, "", m1, h2m2]

        i = 4
        while i >= 0:
            if i!= 2:
                time_numbers.append(int(time[i]))
            i -= 1
        time_numbers = sorted(time_numbers)
        i = 4
        to_replace = True
        time = list(time)
        while i>=0:
            if to_replace and i != 2:
                if i == 1 and time[0] == '2':
                    next_num, to_replace = self.get_next(int(time[i]), list(range(4)), time_numbers)
                else:
                    next_num, to_replace = self.get_next(int(time[i]), ranges[i], time_numbers)
                time[i] = str(next_num)
            i -= 1
        return "".join(time)

sol = Solution()
print(sol.nextClosestTime("19:34"))
print(sol.nextClosestTime("23:59"))
print(sol.nextClosestTime("00:01"))