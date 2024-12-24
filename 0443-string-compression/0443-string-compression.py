class Solution:
    def compress(self, chars: List[str]) -> int:

        #####TODO: without extra space#########
        res = ""
        count = 1
        prev = chars[0]
        
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                res += prev + (str(count) if count > 1 else "")
                prev = chars[i]
                count = 1 
        
        # Handle the last group of characters
        res += prev + (str(count) if count > 1 else "")
        
        chars[:len(res)] = list(res)
        return len(res)