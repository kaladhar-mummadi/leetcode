class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        i = 0
        for num in nums:
            # print(res)
            temp = i ^ num
            res = res ^ temp
            i += 1
        return res
