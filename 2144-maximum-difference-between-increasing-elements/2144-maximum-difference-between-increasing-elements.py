class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for i in range(0, len(nums)):
            
            min_val = min(min_val, nums[i])
            
            max_diff = max(max_diff, nums[i] - min_val)
        
        if max_diff !=0 :
            return max_diff
        else:
            return -1 #no




        