class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []
        
        for s in spells:
            right = len(potions)
            left = 0
            while left< right:
                mid = left + (right - left)//2
                if s*potions[mid] >= success:
                    right = mid
                else:
                    left = mid+1
            res.append(len(potions)-left)
        return res 

            




        