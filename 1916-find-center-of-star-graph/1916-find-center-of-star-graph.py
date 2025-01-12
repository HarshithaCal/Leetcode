class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge0 = edges[0]
        for i in edges[1]:
            if i in edge0:
                return i