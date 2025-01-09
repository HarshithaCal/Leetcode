class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #total TC - O(N^2)
        # i = 0
        # j = 1
        # counter = 0
        # 
        # while j<= len(nums)-1:
        #     print(i, j, nums[i], nums[j])
        #     if nums[i] == nums[j]:
        #         counter+=1
        #         if counter >1:
        #             nums.remove(nums[i])  #TC - O(N)
        #             counter-=1
        #             continue
                                
        #     else:
        #         counter = 0

        #     j+=1
        #     i+=1

        
        ###########TC - O(N)
        write_index = 1  # Position to overwrite the next non-duplicate
        counter = 1  # To track the occurrences of the current element

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index

            
        
        