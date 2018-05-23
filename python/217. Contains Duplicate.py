class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = {}
        for i in nums:
            if i in unique:
                return True
            unique[i] = True
        return False
