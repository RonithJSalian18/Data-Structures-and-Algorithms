class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        x = 0

        for c in str(n):
            d = int(c)
            if d > 0:
                total += d
                x = x * 10 + d

        return total * x