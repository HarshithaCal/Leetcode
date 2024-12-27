class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i] 
            if left_sum == right_sum:
                return i
            # Update left_sum after iteration as we need left_sum till i-1 index for ith index
            left_sum += nums[i]  
        return -1
        