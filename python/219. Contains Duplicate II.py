class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        unique_nums = {}
        i = 0
        for num in nums:
            if num in unique_nums:
                if i - unique_nums[num][-1] <= k:
                    return True
                unique_nums[num].append(i)
            unique_nums[num] = [i]
            i += 1
        return False
