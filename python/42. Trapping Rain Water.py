class Solution(object):
    # Time Limit Exceeded O(n2)
    def brute_force(self, heights):
        ans = 0
        for i in range(1,len(heights)):
            max_left = 0
            max_right = 0
            for j in range(i,-1,-1):
                max_left = max(max_left, heights[j])
            for j in range(i,len(heights)):
                max_right = max(max_right, heights[j])

            ans += min(max_left, max_right) - heights[i]
        return ans
    # store left and right max values instead of calculating each time
    def dp(self, heights):
        if len(heights) == 0:
            return 0
        left_max = [heights[0]]
        right_max = [-1] * len(heights)
        right_max[-1] = heights[-1]
        ans = 0
        temp_max = heights[0]
        for i in range(1,len(heights)):
            temp_max = max(temp_max, heights[i])
            left_max.append(temp_max)
        temp_max = right_max[-1]
        for i in range(len(heights)-2, -1, -1):
            temp_max = max(temp_max, heights[i])
            right_max[i] = temp_max

        for i in range(len(heights)):
            ans += min(left_max[i], right_max[i]) - heights[i]
        return ans



    def trap(self, height):
        return self.dp(height)
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))