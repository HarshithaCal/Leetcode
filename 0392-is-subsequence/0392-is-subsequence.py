class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t) == 0:
            return False

        substr_ptr = 0
        for str_ptr in range(len(t)):
            if t[str_ptr] == s[substr_ptr]:
                substr_ptr +=1
            else:
                str_ptr += 1
            if substr_ptr == len(s):
                return True
            
        return False