class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        len1 = len(word1)
        len2 = len(word2)
        for idx in range(min(len1, len2)):
            merged_str += word1[idx] + word2[idx]
        idx = idx+1
        if len1 > idx:
            merged_str += word1[idx:]
        elif len2 > idx:
            merged_str += word2[idx:]
        else:
            pass
        return merged_str
        