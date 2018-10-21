import math
import sys


class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        min_arr = [nums[0]]
        prev_min = nums[0]
        for num in nums[1:]:
            temp = min(prev_min, num)
            if temp < prev_min:
                prev_min = temp
            min_arr.append(temp)

        stack_arr = []
        j = len(nums)-1
        while j >= 0:
            if nums[j] > min_arr[j]:
                while(len(stack_arr) != 0 and stack_arr[-1] <= min_arr[j]):
                    stack_arr.pop()
                if len(stack_arr) != 0 and stack_arr[-1] < nums[j]:
                    return True

                stack_arr.append(nums[j])
            j -= 1
        return False
