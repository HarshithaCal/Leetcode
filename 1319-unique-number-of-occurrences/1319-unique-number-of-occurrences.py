class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
                #TC - O(n) for set() operation
        return len(freq.values())== len(set(freq.values()))
        