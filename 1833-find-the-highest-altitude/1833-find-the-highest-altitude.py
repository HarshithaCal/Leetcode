class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        prefix_sum = 0 #curr_altitude compared to initial position
        for i in range(len(gain)):
            prefix_sum += gain[i]
            max_alt = max(max_alt, prefix_sum)
        return max_alt
        