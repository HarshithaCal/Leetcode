class Solution:
    def check(self, nums: List[int]) -> bool:
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     if nums[i] > nums[(i + 1) % n]:  # Compare current element with the next (circularly)
        #         count += 1
        #         if count > 1:  # More than one change
        #             return False
        # return True

       
        count=0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                count+=1
        
        return True if count<=1 else False

            