class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = l = r = 0
        for i in s:
            if i == 'L':
                l += 1
            else:
                r += 1
            if r == l:
                c += 1
        return c
        