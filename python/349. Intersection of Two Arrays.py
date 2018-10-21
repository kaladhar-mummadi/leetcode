class Solution(object):
    def intersection(self, nums1, nums2):
        res = set()
        nums1 = set(nums1)
        for i in nums2:
            if i in nums1:
                res.add(i)
        return list(res)