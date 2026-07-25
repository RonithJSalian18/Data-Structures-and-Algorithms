class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(str(n))
        nums = [-int(n) for n in nums]
        heapq.heapify(nums)

        n1 = heapq.heappop(nums)
        n2 = heapq.heappop(nums)
        print(n1, n2)
        return n1 * n2


        