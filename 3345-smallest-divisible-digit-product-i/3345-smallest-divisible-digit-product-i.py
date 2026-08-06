class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 101):
            pro =  1
            cur = num
            while cur != 0:
                digi = cur % 10
                pro = pro * digi
                cur = cur // 10
            if pro % t == 0:
                return num

