class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False # Separate flag for the first row

        # 1. Iterate through matrix to mark the first row and column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # 2. Use the markers to zero out the inner matrix
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 3. Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # 4. Zero out the first row if needed
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0