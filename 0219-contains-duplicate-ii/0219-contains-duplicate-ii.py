class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        for i, v in enumerate(nums):
            if v in a and abs(i - a[v]) <= k:
                return True
            a[v] = i
        return False
