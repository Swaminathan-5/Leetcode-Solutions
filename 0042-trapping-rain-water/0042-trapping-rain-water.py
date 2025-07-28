class Solution:
    def trap(self, he: List[int]) -> int:
        l, r = 0, len(he) - 1
        max_l = he[l]
        max_r = he[r]
        ans = 0
        while l < r:
            if max_l <= max_r:
                ans += max_l - he[l]
                l += 1
                max_l = max(max_l, he[l])
            else:
                ans += max_r - he[r]
                r -= 1
                max_r = max(max_r, he[r])
        return ans