class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def create_subsets(nums, i, subset, subsets):
            if i == len(nums):
                subsets.append(subset[:])
                return 
            
            subset.append(nums[i])
            create_subsets(nums, i+1, subset, subsets)
            subset.pop()

            create_subsets(nums, i+1, subset, subsets)

            return subsets

        create_subsets(nums, 0,[], subsets)


        #compute XOR for each subset:
        result = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total
        return result



        