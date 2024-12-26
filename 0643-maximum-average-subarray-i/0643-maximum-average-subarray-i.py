class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ## Best solution: Sliding window:

        # # Brute-force: TC - O(n*k)
        # max_sum = -999999
        
        # for i in range(len(nums)-k+1):
        #     curr_sum = 0
        #     for j in range(k):
        #         curr_sum += nums[i + j]

        #     if curr_sum > max_sum:
        #         max_sum = curr_sum

        # max_avg = max_sum/k
        # return max_avg
        subSum = sum(nums[:k])
        maxSum = subSum

        for i in range(k, len(nums)):
            subSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, subSum)

        return maxSum / k

            


        