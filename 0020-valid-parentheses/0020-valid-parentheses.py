class Solution:
    def isValid(self, s: str) -> bool:
        mapi = { '(' : ')',
                '[' : ']',
                '{' : '}'
        }
        stack = []
        for i in s:
            if i in mapi:
                stack.append(i)
            else:
                if not stack:
                    return False
                e = stack.pop()
                if mapi[e] != i:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        