class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
            else:
                maxi = max(maxi, curr)
                curr = 0
        return max(maxi, curr)

        