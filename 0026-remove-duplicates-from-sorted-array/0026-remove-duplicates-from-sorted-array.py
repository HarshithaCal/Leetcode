class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while nums and i < len(nums):
            if nums[i-1] == nums[i]:
                removed = nums.remove(nums[i-1])
            else:
                i += 1    
        print(len(nums))
        
        