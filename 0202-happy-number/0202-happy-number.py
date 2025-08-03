class Solution:
    def isHappy(self, n: int) -> bool:
        def find(num):
            return sum(int(d)**2 for d in str(num))
        slow = n
        fast = find(n)
        while fast != 1 and slow != fast:
            slow = find(slow)
            fast = find(find(fast))
        return fast == 1