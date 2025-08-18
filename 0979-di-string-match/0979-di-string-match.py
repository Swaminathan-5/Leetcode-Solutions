class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        res = []
        for i in s:
            if i == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        res.append(l)
        return res
