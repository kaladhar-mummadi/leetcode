from chart_utils import
class Solution(object):
    def permute_backtrack(self, nums, res, pos):

        if pos >= len(nums):
            res.append(list(nums))
            return

        for i in range(pos, len(nums)):
            if i == pos or nums[i] not in nums[pos:i]:
                nums[pos], nums[i] = nums[i], nums[pos]
                self.permute_backtrack(nums, res, pos+1)
                nums[pos], nums[i] = nums[i], nums[pos]

    def permuteUnique(self, nums):
        res = []
        self. permute_backtrack(nums, res, 0)
        return res
sol = Solution()
print(sol.permuteUnique([1,1,2,2]))