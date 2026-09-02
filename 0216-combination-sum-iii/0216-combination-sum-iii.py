class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, score):
            if score == n and len(cur) == k:
                res.append(cur[:])
                return

            if i > 9 or score > n or len(cur) == k:
                return

            cur.append(i)
            backtrack(i+1, cur, score + i)
            cur.pop()

            backtrack(i+1, cur, score)

        backtrack(1, [], 0)
        return res
