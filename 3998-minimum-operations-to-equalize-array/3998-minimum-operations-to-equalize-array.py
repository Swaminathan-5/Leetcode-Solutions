class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = nums.count(nums[0])
        return 1 if c < len(nums) else 0