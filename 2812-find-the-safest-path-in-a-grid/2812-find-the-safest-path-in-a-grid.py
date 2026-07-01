class Solution:
    # 4-directional movement
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def maximumSafenessFactor(self, A: List[List[int]]) -> int:
        # If start/end has a thief
        if A[0][0] or A[-1][-1]:
            return 0

        n, q = len(A), deque()

        # Add all thieves as BFS sources
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    q.append((i, j))

        # Multi-source BFS to compute distance from nearest thief
        while q:
            i, j = q.popleft()
            v = A[i][j]

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if min(x, y) >= 0 and max(x, y) < n and not A[x][y]:
                    A[x][y] = v + 1
                    q.append((x, y))

        # Max heap: prioritize path with highest safeness
        pq = [(-A[0][0], 0, 0)]

        while pq:
            sf, i, j = heapq.heappop(pq)
            sf = -sf

            # Reached destination
            if i == n - 1 and j == n - 1:
                return sf - 1

            # Explore neighbors
            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if min(x, y) >= 0 and max(x, y) < n and A[x][y] > 0:
                    heapq.heappush(pq, (-min(sf, A[x][y]), x, y))
                    A[x][y] *= -1  # Mark visited

        return A[n - 1][n - 1] - 1