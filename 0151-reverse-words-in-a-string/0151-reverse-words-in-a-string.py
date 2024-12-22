class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()  # Split the string into words
        s.reverse()       # Reverse the list of words
        print(s)
        return " ".join(s)  # Join the reversed words with a single space

        