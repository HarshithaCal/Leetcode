class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        #### Optimal approach - using sets:
        ### set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average.
        longest = 1

        st=set()
        
        for i in range(len(nums)):
            st.add(nums[i])

        
        #check if nums can be a starting point
        for item in st:
            if item-1 not in st:
                cnt=1
                x = item
                while x+1 in st:
                    cnt +=1
                    x+=1
                longest = max(longest, cnt)
        return longest
                


        
        # #TC - O(N*logN)
        # nums.sort()
        # max_len = 1
        # curr_len = 1
        # prev_num = nums[0]
        # for i in range( 1, len(nums)):
        #     if nums[i]== prev_num+1:
        #         curr_len += 1
        #         max_len = max(max_len, curr_len)
            
        #     elif nums[i] == prev_num:
        #         pass
        #     else:
        #         curr_len = 1
        #     prev_num = nums[i]
        #     # print(f"idx: {i}, prev_num: {prev_num}, nums[i]: {nums[i]}, curr_len = {curr_len}")
        
        # return max_len

        