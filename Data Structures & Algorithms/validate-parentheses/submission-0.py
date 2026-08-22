class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            try:
                if p in ['(', '{', '[']:
                    stack.append(p)
                else:
                    close = stack.pop()
                    if (close == '(' and p != ')') or (close == '{' and p != '}') or (close == '[' and p != ']'):
                        return False
            except:
                return False
        return len(stack) == 0