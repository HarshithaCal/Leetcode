class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, is_search_left):
            left = 0
            right = len(nums) -1
            idx = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    idx = mid
                    if is_search_left:
                        right = mid -1
                    else:
                        left = mid + 1
                    

                elif nums[mid] < target:
                    left = mid +1
                else:
                    right = mid-1
            return idx

        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)

        return [left, right]
