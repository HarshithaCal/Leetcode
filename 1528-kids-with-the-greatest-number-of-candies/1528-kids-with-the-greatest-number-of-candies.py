class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        res = []
        for nCandies in candies:
            if nCandies + extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)
        return res
        
        