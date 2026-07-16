class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # To keep track of visited cells in the current DFS path

        def dfs(r, c, i):
            # 1. Goal (Base Case: Found all characters)
            if i == len(word):
                return True
            
            # 2. Constraints (Out of bounds, character mismatch, or already visited)
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # 3. Make a Choice (Add current cell to path)
            path.add((r, c))
            
            # 4. Explore all 4 directions recursively
            res = (dfs(r + 1, c, i + 1) or  # Down
                   dfs(r - 1, c, i + 1) or  # Up
                   dfs(r, c + 1, i + 1) or  # Right
                   dfs(r, c - 1, i + 1))    # Left
            
            # 5. Undo the Choice (Backtrack)
            path.remove((r, c))
            
            return res

        # Iterate through every cell in the grid to find a starting point
        for r in range(ROWS):
            for c in range(COLS):
                # If we find a valid path starting from (r, c), return True immediately
                if dfs(r, c, 0):
                    return True
                    
        return False