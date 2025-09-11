class Solution:
    def sortVowels(self, s: str) -> str:
        vow = 'aeiouAEIOU'
        res = [i for i in s if i in vow]
        res.sort()
        l = list(s)
        j = 0
        for i in range(len(l)):
            if s[i] in vow:
                l[i] = res[j]
                j += 1
        return ''.join(l)