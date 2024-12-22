class Solution:
    def reverseVowels(self, s: str) -> str:
      
        # time complexity - O(N)
        ans = ""
        vowels = []
        index = []
        for idx, char in enumerate(s):
            if char in "aeiouAEIOU":
                vowels.append(char)
                index.append(idx)
        
        vowels.reverse()
        ans = list(s)  # Use a list for mutable operations
        #without this time limit exceeds
        
        j = 0
        for i in index:  
            ans[i] = vowels[j]
            j += 1
        
        return ''.join(ans)
            
