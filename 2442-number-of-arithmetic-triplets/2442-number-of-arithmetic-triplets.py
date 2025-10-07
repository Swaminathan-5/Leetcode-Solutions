class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s, c = set(nums), 0
        for i in nums:
            if i + diff in s and i + 2 * diff in s:
                c += 1
        return c