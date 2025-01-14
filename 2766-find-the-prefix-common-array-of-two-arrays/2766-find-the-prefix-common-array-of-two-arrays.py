class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []
        i = 0
        freq_A = {}
        count = 0
        while i<len(A):
            if A[i] in freq_A: 
                count += 1   #missed this
            else:
                freq_A[A[i]] = 1
            
            if B[i] in freq_A:
                count+= 1
            else:
                freq_A[B[i]] = 1
            
            c.append(count)
            i+=1 
        return c
            

            
            
        
            

            
                

        