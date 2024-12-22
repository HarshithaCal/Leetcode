class Solution:
    def reverseVowels(self, s: str) -> str:

        #time limit exceeded
        ans = ""
        vowels = []
        index = []
        for idx, char in enumerate(s):
            if char in "aeiouAEIOU":
                vowels.append(char)
                index.append(idx)
        
        vowels.reverse()
        ans = list(s)  # Use a list for mutable operations
        
        j = 0
        for i in index:  # Iterate over indices of vowels only
            ans[i] = vowels[j]
            j += 1
        
        return ''.join(ans)
            
