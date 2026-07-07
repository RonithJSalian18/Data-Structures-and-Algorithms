class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        nums = list(str(n))
        summ = 0
        val = ''

        for ch in nums:
            if ch != "0":
                summ += int(ch)
                val += ch

        return summ * int(val)
        