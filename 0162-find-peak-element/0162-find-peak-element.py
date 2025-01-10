class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        ##########tc - o(log n) - Binary search
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check the relationship between nums[mid] and nums[mid + 1]
            if nums[mid] > nums[mid + 1]:
                # Peak is in the left half (including mid)
                right = mid
            else:
                # Peak is in the right half
                left = mid + 1

        # Left and right converge to the peak element
        return left



        # #TC - O(N)
        # n = len(nums)

        # # Edge case: Single element
        # if n == 1:
        #     return 0

        # # Edge case: Two elements
        # if n == 2:
        #     return 0 if nums[0] > nums[1] else 1

        # for i in range(1, n - 1):
        #     if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        #         return i

        # # Check the boundaries - key!!
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[n - 1] > nums[n - 2]:
        #     return n - 1
