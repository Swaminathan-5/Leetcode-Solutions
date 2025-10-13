class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        max_length = 0
        n = len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            w = (r - l) + 1
            max_length = max(max_length, w)
            sett.add(s[r])
        return max_length