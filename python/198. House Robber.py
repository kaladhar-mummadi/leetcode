class Solution:
    def rob(self, nums):
        res = 0
        if len(nums) == 0:
            return res
        if len(nums) <= 2:
            return max(nums)
        max_rob = max(nums[0], nums[1])
        secondLeft = nums[0]
        for i in range(2,len(nums)):
            res = max(max_rob, secondLeft+nums[i])
            secondLeft = max_rob
            max_rob = res
        return res
sol = Solution()
print(sol.rob([2,1,1,2]))