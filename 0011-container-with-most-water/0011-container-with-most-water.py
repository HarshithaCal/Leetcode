class Solution:
    def maxArea(self, height: List[int]) -> int:
        #two-pointer approach: TC - O(N)
        left = 0                
        right = len(height) - 1 
        max_area = 0           

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)
            
            # Main logic:Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # ## Brute-force approach
        # n = len(height)
        # max_area = 0
        
        # # Iterate through all pairs of lines
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         h = min(height[i], height[j])
        #         w = j - i
        #         area = h * w
        #         max_area = max(max_area, area)
        
        # return max_area
        


        

        