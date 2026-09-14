class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        res = []

        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        for val, freq in counter.items():
            if freq == 1:
                res.append(val)

        return res 
        