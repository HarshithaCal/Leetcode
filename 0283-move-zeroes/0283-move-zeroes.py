class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zp], nums[i] = nums[i], nums[zp]
                zp +=1
