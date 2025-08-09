class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        maps = {}
        for i, j in zip(s, t):
            if (i in hashs and hashs[i] != j) or (j in maps and maps[j] != i):
                return False
            hashs[i] = j
            maps[j] = i
        return True