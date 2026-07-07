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
            elif i in mapi.values():
                if stack:
                    e = stack.pop()
                else:
                    return False
                if mapi[e] != i:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        