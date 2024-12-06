class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        miss = expected_sum - actual_sum
        return miss


        # d = {}
        # for e in nums:
        #     d[e] = 1
        
        # for i in range(0, len(nums)+1):
        #     if i not in d.keys():
        #         return i
        