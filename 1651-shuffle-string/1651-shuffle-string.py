class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = [''] * len(s)
        for i, j in enumerate(s):
            r[indices[i]] = j
        return ''.join(r)
