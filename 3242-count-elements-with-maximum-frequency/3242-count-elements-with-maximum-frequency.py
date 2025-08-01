class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = {}
        count = 0
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        s = max(a.values())
        count = 0
        for i in a.values():
            if i == s:
                count += i
        return count
        