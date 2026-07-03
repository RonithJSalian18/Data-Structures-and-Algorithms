class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        res = []

        for n in nums:
            if n not in s:
                s.add(n)
            else:
                res.append(n)

        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)

        return res