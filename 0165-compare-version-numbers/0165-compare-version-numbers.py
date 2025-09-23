class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        a, b = v1.split('.'), v2.split('.')
        x = tuple(map(int, a + ['0'] * (len(b) - len(a))))
        y = tuple(map(int, b + ['0'] * (len(a) - len(b))))
        return (x > y) - (x < y)
