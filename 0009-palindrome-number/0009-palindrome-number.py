class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # # print(x[::-1])
        # for i in range(ceil(len(x)/2)):
        #     if x[i] != x[-i-1]:
        #         return False

        # return True

        # OR 
        x = str(x)
        return x==x[::-1]
        