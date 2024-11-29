class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Brute force 
        # - make a set - to get distinct elements       #TC - O(N logN)
        # - add the elements from set to the List back  #TC - O(N)
        # So, total is O(N*logN) + O(N), SC - O(N) - Set

        #Two pointer approach
        i = 0
        j = 1
        n = len(nums)
        for j in range(0, n):

            if nums[i] != nums[j]:
                # we got unique ele not present in arr[:i] so add it to the arr
                i += 1
                nums[i] = nums[j]
            # elif nums[i] == nums[j]:
            #     # do nothing 
        return i+1    



        #mine - TC - O(N) and SC - O(1)
        # i = 1
        
        # while nums and i < len(nums):
        #     if nums[i-1] == nums[i]:
        #         removed = nums.remove(nums[i-1])
        #     else:
        #         i += 1    
        # print(len(nums))
        
        