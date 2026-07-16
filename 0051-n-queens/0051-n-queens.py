class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Hash sets to track our constraints in O(1) time
        col = set()
        posDiag = set() # Tracks positive diagonals (row + col)
        negDiag = set() # Tracks negative diagonals (row - col)
        
        res = []
        # Initialize an empty N x N board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # 1. Goal (Base Case): If we successfully placed a queen in every row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # 2. Explore Choices: Try placing a queen in every column 'c' for the current row 'r'
            for c in range(n):
                # 3. Constraints (Pruning): Is this cell under attack?
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # Skip this cell, it's invalid
                
                # Make a Choice: Place the queen and update attack zones
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # Recurse: Move to the next row
                backtrack(r + 1)
                
                # Undo the Choice (Backtrack): Remove the queen and free up the attack zones
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        # Start the backtracking process at row 0
        backtrack(0)
        return res