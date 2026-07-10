class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        start = mid = end = False

        for i, j, k in triplets:
            if (i > target[0]) or (j > target[1]) or (k > target[2]):
                continue
            if i == target[0]:
                start = True
            if j == target[1]:
                mid = True
            if k == target[2]:
                end = True

        return start and end and mid
        