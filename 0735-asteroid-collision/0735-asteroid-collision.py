class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Initialize the stack
        
        for curr in asteroids:
            while stack and curr < 0 < stack[-1]:  # Check for a collision scenario
                prev = stack.pop()
                if abs(curr) > abs(prev):  # Current asteroid is larger
                    continue
                elif abs(curr) == abs(prev):  # Both explode
                    curr = 0
                    break
                else:  # Previous asteroid is larger
                    curr = 0
                    stack.append(prev)
                    break
            if curr:  # Add asteroid to stack if it still exists
                stack.append(curr)
        return stack


            
  
            