class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = candidates
        n = len(nums)

        def backtrack(i, cursum):
            if cursum == target:
                res.append(sol[:])
                return 

            if cursum > target or i == n:
                return

            backtrack(i + 1, cursum)

            sol.append(nums[i])
            backtrack(i, cursum + nums[i])
            sol.pop()

        backtrack(0, 0)
        return res
        