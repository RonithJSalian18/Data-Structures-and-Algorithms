from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))

        rank = {}
        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1

        res = []
        for n in arr:
            res.append(rank[n])
        
        return res