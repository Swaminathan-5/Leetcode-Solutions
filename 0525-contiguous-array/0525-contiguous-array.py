class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = res = 0
        d = {}
        for i, v in enumerate(nums):
            if v == 0:
                pre -= 1
            else:
                pre += 1
            if pre == 0:
                res = max(res, i + 1)
            if pre not in d:
                d[pre] = i
            else:
                res = max(res, i - d[pre])
        return res