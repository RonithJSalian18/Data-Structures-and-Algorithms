class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        positions = set(nums)

        for i in range(len(moveFrom)):
            fr = moveFrom[i]
            to = moveTo[i]

            positions.remove(fr)
            positions.add(to)

        return sorted(list(positions))