class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        largest = 0
        heapq.heapify(nums)

        while k > 0:
            largest = heapq.heappop(nums)
            k -= 1

        return -largest
        