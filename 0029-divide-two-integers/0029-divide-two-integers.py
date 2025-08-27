class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = math.trunc(dividend / divisor)
        if quotient > (2**31) - 1:
            return quotient - 1
        else:
            return quotient