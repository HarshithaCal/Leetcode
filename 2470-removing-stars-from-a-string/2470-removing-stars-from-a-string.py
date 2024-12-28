class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
                else:
                    return "* is at the start"
            else:
                stack.append(char)

        str_stack = "".join(stack)
        return str_stack
        