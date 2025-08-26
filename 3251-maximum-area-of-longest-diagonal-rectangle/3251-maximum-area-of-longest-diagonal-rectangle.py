class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mins = diag = 0
        for i, j in dimensions:
            d = (i ** 2 + j ** 2) ** 0.5
            area = i * j
            if d > mins:
                mins = d
                diag = area
            elif d == mins:
                diag = max(diag, area)
        return diag

