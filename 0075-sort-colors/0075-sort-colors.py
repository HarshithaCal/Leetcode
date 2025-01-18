class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Optimal approach:
        ####  Dutch National flag algorithm. 
        low = 0
        high = len(nums)-1
        mid = 0 #used for traversal 

        while mid<=high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid +=1
            
            elif nums[mid]==1:
                mid+= 1
            
            elif nums[mid]==2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -=1
        return nums



        # ###TC - O(2*N) and SC -O(1)
        # count0 = 0
        # count1=0
        # count2 = 0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         count0 += 1
        #     elif nums[i] == 1:
        #         count1 +=1
        #     else:
        #         count2 +=1 
        # for i in range(count0+count1+count2):
        #     if i< count0:
        #         nums[i]=0
        #     elif i>=count0 and i<count0+ count1:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        
        # return nums
        
         
        