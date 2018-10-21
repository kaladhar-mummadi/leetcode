class Solution(object):
    def rec_helper(self, nums, total_sum, n, prev_sum):
        if prev_sum == total_sum:
            return True
        elif prev_sum > total_sum or n < 0:
            return False
        sum_inc = prev_sum + nums[n]
        sum_exc = prev_sum
        return self.rec_helper(nums, total_sum, n - 1, sum_inc) or self.rec_helper(nums, total_sum, n - 1, sum_exc)

    def canPartition(self, nums):
        tot_sum = sum(nums)
        sorted_nums = sorted(nums)
        if tot_sum % 2 != 0:
            return False
        else:
            return self.rec_helper(nums, tot_sum / 2, len(sorted_nums)-1, 0)



solution = Solution()
print(solution.canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,97,95]))
# print(solution.canPartition([1,5,11,5]))
