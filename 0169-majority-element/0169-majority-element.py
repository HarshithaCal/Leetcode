class Solution:
    def majorityElement(self, nums: List[int]) -> int:

    #Boyer–Moore majority  
        candidate = -1
        votes = 0
        for i in range(len(nums)):
            if votes==0:
                candidate = nums[i]
                votes = 1
            
            else:
                if nums[i] != candidate:
                    votes -= 1
                else:
                    votes += 1
            
        return candidate

            