class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = Counter(nums)
        c = 0
        for i in a.values():
            c += i * (i - 1) // 2
        return c