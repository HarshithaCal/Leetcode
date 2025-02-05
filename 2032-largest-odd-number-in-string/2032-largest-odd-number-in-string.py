class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_index = len(num)-1
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2 == 0:
                last_index -= 1
            else:
                return num[:last_index+1]

        return ""