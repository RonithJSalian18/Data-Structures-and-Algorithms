class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m, n = len(image), len(image[0])
        val = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] == color:
                return
            elif image[i][j] == val:
                image[i][j] = color
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        dfs(sr, sc)
        return image