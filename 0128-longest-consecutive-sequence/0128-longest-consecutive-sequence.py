class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_len = 1
        curr_len = 1
        prev_num = nums[0]
        for i in range( 1, len(nums)):
            if nums[i]== prev_num+1:
                curr_len += 1
                max_len = max(max_len, curr_len)
            
            elif nums[i] == prev_num:
                pass
            
            else:
                curr_len = 1

            prev_num = nums[i]
            # print(f"idx: {i}, prev_num: {prev_num}, nums[i]: {nums[i]}, curr_len = {curr_len}")
        
        return max_len

        