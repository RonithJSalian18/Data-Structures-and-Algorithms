class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashMap = {}
        n = len(edges)

        for i in range(len(edges)):
            for j in range(len(edges[i])):
                v = edges[i][j]
                hashMap[v] = 1 + hashMap.get(v, 0)

        for val, freq in hashMap.items():
            if freq == n:
                return val
        