class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
            if c not in pairs: # not a closing bracket
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    # if the stack is empty, these is no matching opening bracket
                    # if the top of the stack is not the correct matching bracket,
                    # it is also invalid
                    return False
                stack.pop() # remove the matching opening bracket from the stack
        
        # if the stack is empty, every opening bracket was matched properly
        # thus return True
        # if it is not empty, some opening brackets were never closed
        return not stack
        
