class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pp = 0
        for i in range(len(nums) // 2):
            pairs = nums[i] + nums[len(nums) - 1 - i]
            pp = max(pp, pairs)
        return pp