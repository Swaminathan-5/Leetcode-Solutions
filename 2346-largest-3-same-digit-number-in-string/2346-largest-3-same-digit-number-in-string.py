class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                subs = num[i:i + 3]
                if subs > max_good:
                    max_good = subs
        return max_good