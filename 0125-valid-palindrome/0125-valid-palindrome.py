class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    ###another  solution   
    # s =''.join(filter(str.isalnum, s.lower()))
    #     return s[::-1]==s

        s = "".join([char.lower() for char in s if char.isalnum()])
        l= 0
        r = len(s) - 1
        while l<r:
            if s[l] != s[r]:
                return False
            l+= 1
            r-=1
        
        return True


        