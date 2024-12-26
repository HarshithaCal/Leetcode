class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Edge case: If k == len(s), calculate vowels for the whole string
        if len(s) <= k:
            return sum(1 for char in s if char in "aeiou")

        vowels = set("aeiou")
        max_counter = 0
        counter = 0

        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                counter += 1
        max_counter = counter

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                counter += 1
            if s[i - k] in vowels:
                counter -= 1
            max_counter = max(max_counter, counter)

        return max_counter
