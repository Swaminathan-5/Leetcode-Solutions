class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        a = 0
        for i, v in enumerate(nums):
            if a == s - a - v:
                return i
            a += v
        return -1 