class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()  # Split the string into words
        s.reverse()  
        print(s)
        return " ".join(s)

        