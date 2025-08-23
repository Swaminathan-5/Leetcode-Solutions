class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        c = b = True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                c = False
            if s2[i] < s1[i]:
                b = False
        return c or b