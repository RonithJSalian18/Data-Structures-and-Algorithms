class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order = []

        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITED, VISITING = 0, 2, 1
        states = [UNVISITED] * numCourses

        def dfs(i):
            state = states[i]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
