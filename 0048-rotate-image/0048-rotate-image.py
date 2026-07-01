class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = []

        for r in range(len(matrix)):
            mat = []
            for c in range(len(matrix[0])):
                mat.append(matrix[c][r])
            res.append(mat[::-1])
        matrix[:] = res