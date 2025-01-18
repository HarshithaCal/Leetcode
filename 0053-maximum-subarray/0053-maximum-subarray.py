class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window approach 
        left = 0
        right = 0
        curr_sum = 0
        max_sum = -99999

        while right <len(nums):
            curr_sum += nums[right]
            
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
                left= right+1
            
            right +=1

        return max_sum

            



        
        