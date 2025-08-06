class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for i in s:
            if i in odd:
                odd.remove(i)
            else:
                odd.add(i)
        if len(odd) > 0:
            return len(s) - len(odd) + 1
        else:
            return len(s)