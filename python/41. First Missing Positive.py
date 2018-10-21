class Solution(object):
    def by_sorting(self, nums):
        nums = sorted(list(set(nums)))
        i = 0
        gotOne = False
        for num in nums:
            if num == 1:
                gotOne = True
                break
            i += 1
        if not gotOne:
            return 1
        j = 1
        while i < len(nums):
            # print(j)
            if j != nums[i]:
                break
            j += 1
            i += 1

        return j
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

