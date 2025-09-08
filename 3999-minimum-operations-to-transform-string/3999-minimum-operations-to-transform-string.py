class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        for i in s:
            a = (26 - (ord(i) - ord('a'))) % 26
            res = max(res, a)
        return res