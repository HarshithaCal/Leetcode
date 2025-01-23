class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x)
        for i in range(ceil(len(x)/2)):
            if x[i] != x[-i-1]:
                return False

        return True
        