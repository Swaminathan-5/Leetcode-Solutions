from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = Counter(nums)
        maxs = max(a.values())
        return sum(i for i in a.values() if i == maxs)