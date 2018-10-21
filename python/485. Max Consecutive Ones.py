class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        if len(nums) == 0:
            return  0
        consec_count = 0
        max_len = 0
        for i in nums:
            if i == 0:
                if max_len < consec_count:
                    max_len = consec_count
                consec_count = 0

            else:
                consec_count += 1
        if max_len < consec_count:
            max_len = consec_count

        return max_len


sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0]))