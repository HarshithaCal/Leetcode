class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
     # Step 1: Initialize the window
        left = 0
        zero_count = 0
        max_length = 0
        
        # Step 2: Expand and update the window
        for right in range(len(nums)):
            # Include the current element in the window
            if nums[right] == 0:
                zero_count += 1
            
            # If the number of 0s exceeds k, shrink the window: Main logic
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length   