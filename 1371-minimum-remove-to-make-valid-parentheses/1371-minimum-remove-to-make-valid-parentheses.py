class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: remove invalid ')'
        res = []
        open_count = 0
        for char in s:
            if char == '(':
                open_count += 1
                res.append(char)
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                    res.append(char)
            else:
                res.append(char)
        
        # Pass 2: remove extra '('
        final_res = []
        open_to_remove = open_count
        for char in reversed(res):
            if char == '(' and open_to_remove > 0:
                open_to_remove -= 1
                continue
            final_res.append(char)
        
        return "".join(reversed(final_res))
