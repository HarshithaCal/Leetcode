class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_counter = 0
        max_ones = 0
        l = len(nums)

        for right in range(l):
            if nums[right] == 0:
                zero_counter += 1

            while zero_counter > 1:  # Shrink the window when there are more than one 0
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1

            # Update max_ones excluding the one element we would delete
            max_ones = max(max_ones, right - left)

        return max_ones


        
        