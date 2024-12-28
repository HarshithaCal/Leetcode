class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if both strings have the same set of unique characters
        if set(word1) != set(word2):
            return False
        
        # Count character frequencies
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Check if both words have the same set of characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Check if the sorted frequency values match
        return sorted(freq1.values()) == sorted(freq2.values())

        #########Same logic ..
        # if len(word1) != len(word2):
        #     return False
        
        # # frequencies for both words
        # freq1 = {}
        # freq2 = {}
        
        # for char in word1:
        #     # freq1[char] = freq1.get(char, 0) + 1
        #     if char in freq1:
        #         freq1[char] += 1
        #     else:
        #         freq1[char] = 1
        # for char in word2:
        #     freq2[char] = freq2.get(char, 0) + 1
        
        # # Check if both words have the same set of characters
        # if set(freq1.keys()) != set(freq2.keys()):
        #     return False
        # # print(f"freq1: {freq1} and freq2: {freq2}")
        # # print(f"freq1 values: {freq1.values()} and freq2 values: {freq2.values()}")

        # # Check if sorted frequency values match
        # if sorted(freq1.values()) != sorted(freq2.values()):
        #     return False
        
        # return True
        