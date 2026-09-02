class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, amt):
            if amt == target:
                res.append(sol[:])
                return
            
            if amt > target or i == len(candidates):
                return

            backtrack(i+1, amt)

            sol.append(candidates[i])
            backtrack(i, amt + candidates[i])
            sol.pop()

        backtrack(0,0)
        return res