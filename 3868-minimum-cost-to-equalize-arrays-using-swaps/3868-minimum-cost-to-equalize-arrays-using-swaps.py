class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        if counter1 == counter2:
            return 0

        total = counter1 + counter2

        cost = 0
        for k in total:
            if total[k] % 2 != 0:
                return -1

            diff = total[k] // 2
            if counter1[k] > diff:
                cost += counter1[k] - diff

        return cost