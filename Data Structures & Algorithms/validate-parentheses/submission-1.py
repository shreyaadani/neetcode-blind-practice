class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in closetoopen:
                if not stack or stack[-1]!= closetoopen[c]:
                    return False
                stack.pop()

            else:
                stack.append(c)

        return True if not stack else False               
