class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        want = 1
        for i in nums:
            if i == want:
                want += 1
            elif i > want:
                return want
        return want