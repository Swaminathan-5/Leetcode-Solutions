class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, c in enumerate(citations):
            if n - i <= c:
                return n - i
        return 0
        