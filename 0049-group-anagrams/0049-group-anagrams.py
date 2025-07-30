class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s not in res:
                res[s] = []
            res[s].append(i)
        return list(res.values())