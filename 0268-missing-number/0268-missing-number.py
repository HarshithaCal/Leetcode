class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        for e in nums:
            d[e] = 1
        
        for i in range(0, len(nums)+1):
            if i not in d.keys():
                return i
        