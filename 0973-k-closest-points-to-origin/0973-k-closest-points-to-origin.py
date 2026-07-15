class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sq = []

        for x, y in points:
            val = x*x + y*y
            sq.append([val, x, y])

        heapq.heapify(sq)
        res = []
        
        while k > 0:
            val, x, y = heapq.heappop(sq)
            res.append([x, y])
            k -= 1

        return res