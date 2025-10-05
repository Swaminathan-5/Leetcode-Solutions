class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r, res = 0, len(people)-1, len(people)
        while l < r:
            if people[l] + people[r] <= limit:
                res -= 1
                l += 1
            r -= 1
        return res