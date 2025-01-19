class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid +1
        # If the target isn't found, the left pointer ends up pointing to the smallest index where the target can be inserted without breaking the order.
        return left




        

        