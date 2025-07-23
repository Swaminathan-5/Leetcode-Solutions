class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        t, r = 0, 0
        for i in range(len(nums)):
            t += nums[i]
            avg = (t + i) // (i + 1)
            r = max(r, avg)
        return r
            
