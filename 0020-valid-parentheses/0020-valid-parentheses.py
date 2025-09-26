class Solution:
    def isValid(self, s: str) -> bool:
        # use of list as our stack
        stack = []
        # dict to hold matching pairs
        mapping = {")": "(", "}": "{", "]":"["}
        # iterate through each char in the string
        for char in s:
            # if the char is a closing bracket
            if char in mapping:
                # get the top of the stack or dummy char if the stack is empty
                top = stack.pop() if stack else '#'

                # check for a match, if it's not a match, or the stack was empty
                if mapping[char] != top:
                    return False
            else:
                # if it's an opening bracket, push it onto the stack
                stack.append(char)
        # after the loop, the stack must be empty for the string to be valid
        return not stack
