class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        ##### Optimized backtracking approach - perform XOR while performing backtracking
        #TC - O(2^N) and SC - O(N)
        def subset_XOR_sum(nums, i, current_XOR):
            if i == len(nums):
                return current_XOR

            with_ele = subset_XOR_sum(nums, i+1, current_XOR^nums[i])

            without_ele = subset_XOR_sum(nums, i+1, current_XOR)

            return with_ele + without_ele

        return subset_XOR_sum(nums, 0, 0)



        ############## Approach 1
        # #  overall space complexity is O(n+((n/2).2^n))
        # #overall time complexity is O(2^n + ((n/2).2^n))
        # subsets = []
        # def create_subsets(nums, i, subset, subsets):
        #     if i == len(nums):
        #         subsets.append(subset[:])
        #         return 
            
        #     subset.append(nums[i])
        #     create_subsets(nums, i+1, subset, subsets)
        #     subset.pop()

        #     create_subsets(nums, i+1, subset, subsets)
        #     return subsets

        # create_subsets(nums, 0,[], subsets)

        # #compute XOR for each subset:
        # result = 0
        # for subset in subsets:
        #     subset_XOR_total = 0
        #     for num in subset:
        #         subset_XOR_total ^= num
        #     result += subset_XOR_total
        # return result



        