class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4          # Target side length
        sides = [0] * 4                         # Current length of 4 sides

        if sum(matchsticks) / 4 != length:      # Total must divide by 4
            return False
        matchsticks.sort(reverse = True)
        def backtrack(i):
            if i == len(matchsticks):           # All sticks placed
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:  # Fits this side
                    sides[j] += matchsticks[i]          # Add stick

                    if backtrack(i + 1):                # Place next stick
                        return True

                    sides[j] -= matchsticks[i]          # Undo choice

            return False

        return backtrack(0)                     # Start from first stick