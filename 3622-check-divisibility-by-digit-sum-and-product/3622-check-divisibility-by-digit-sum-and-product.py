class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi, multi = 0, 1
        val = n

        while n != 0:
            digit = n % 10
            sumi += digit
            multi *= digit
            n = n // 10
        
        if val % (sumi + multi) == 0:
            return True
        else:
            return False