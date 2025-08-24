class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxs = left = zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxs = max(maxs, i - left)
        return maxs