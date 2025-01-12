class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        
        #one of the end points will be used - key!!!
        for j in range(len(colors)):
            if colors[j] != colors[0]:
                max_dist = max(max_dist, j)
            if colors[j] != colors[-1]:
                max_dist = max(max_dist, len(colors)-j-1)
        
        return max_dist


        