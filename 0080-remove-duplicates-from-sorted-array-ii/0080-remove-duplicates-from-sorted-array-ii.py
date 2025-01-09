class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        counter = 0
        print(len(nums))
        while j<= len(nums)-1:
            print(i, j, nums[i], nums[j])
            if nums[i] == nums[j]:
                counter+=1
                if counter >1:
                    nums.remove(nums[i])
                    counter-=1
                    continue
                                
            else:
                counter = 0

            j+=1
            i+=1

            
        
        