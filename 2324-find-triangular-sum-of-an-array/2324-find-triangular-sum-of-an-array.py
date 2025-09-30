import math
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            c = math.comb(n - 1, i)
            res += c * nums[i]
        return res % 10