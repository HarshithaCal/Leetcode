class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # size of freq wont be greater than 26 so the SC = O(1)
        # TC - O(N)
        freq = {}
        if len(s)!= len(t):
            return False
        
        else:
            for i in range(len(s)):
                if s[i] in freq:
                    freq[s[i]] += 1
                else:
                    freq[s[i]] = 1
            
                if t[i] in freq:
                    freq[t[i]] -= 1
                
                else:
                    freq[t[i]] = -1
        for i in freq.values():
            if i!= 0:
                return False
        return True


        