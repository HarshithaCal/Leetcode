class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #different approach - sets - O(n+m) and same space complexity - O(n+m)
        
        # Convert nums1 and nums2 to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # Find unique elements
        answer = [
            list(set1 - set2),  # Elements in nums1 but not in nums2
            list(set2 - set1)   # Elements in nums2 but not in nums1
        ]

        return answer

        # #TC - O(n+m)
        # answer = [[] for _ in range(2)]
        # maps = {}
        # for x in nums1:
        #     if x not in maps: #x not in maps involves a hash table lookup, which is O(1) on average
        #         maps[x] = 1

        # #be cautious about the mulitple occurrence of the same element
        # for y in nums2:
        #     if y in maps:
        #         if maps[y] == 1:  # Element is in nums1, mark as common
        #             maps[y] = 0
        #     else:
        #         maps[y] = 2

        # for key in maps:
        #     if maps[key] == 1: 
        #         answer[0].append(key)
        #     elif maps[key] == 2: # value = 2 .i.e, nums2 unique elements
        #         answer[1].append(key)
        #     else:
        #         pass
        # return answer
            
        

        