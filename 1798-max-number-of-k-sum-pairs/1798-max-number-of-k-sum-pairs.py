class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
#dictionary / hashmap logic
        counter = 0
        dicti = {}
        for x in nums:
            complement = k-x
            if complement in dicti and dicti[complement] > 0:
                counter +=1
                dicti[complement] -= 1
            else:
                #frequency logic
                if x in dicti:
                    dicti[x] += 1
                else:
                    dicti[x] = 1
        return counter

        # #Brute force: - O(n^2)
        # counter = 0
        # i = 0
        # #use while loop whenever we are changing the length of the lists.
        # while i < len(nums):
        #     j = i+1
        #     while j < len(nums):
        #         if i != j and nums[i] + nums[j] == k:
        #             #order in which pop() happens is important, to avoid the index shifting
        #             nums.pop(j)
        #             nums.pop(i)
        #             counter += 1
        #             #to avoid missing out some elements
        #             j =i
        #         else:
        #             j+=1
        #     i+=1
        # return counter


        