class Solution:
    def splitNum(self, num: int) -> int:
        a = sorted(list(map(int, str(num))))
        return int(''.join(map(str, a[::2]))) + int(''.join(map(str, a[1::2])))
        