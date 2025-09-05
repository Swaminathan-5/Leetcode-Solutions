class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right