class Solution:
    def reverseWords(self, s: str) -> str:
        #TC - O(N)
        s = s.split()  # Split the string into words
        # s.split(" ") # includes the extra spaces as well
        s.reverse()  #s.reverse() is inplace
        print(s)
        return " ".join(s)

        