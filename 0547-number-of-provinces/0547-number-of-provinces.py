class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

            return

        for i in range(len(isConnected)):
            if i not in visited:
                province += 1
                dfs(i)

        return province