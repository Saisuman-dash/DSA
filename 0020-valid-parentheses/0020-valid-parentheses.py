class Solution:
    def isValid(self, s: str) -> bool:
        map = { '(' : ')',
                '[' : ']',
                '{' : '}'
        }
        stack = []
        for i in s:
            if i in map:
                stack.append(i)
            elif i in map.values():
                if stack:
                    e = stack.pop()
                else:
                    return False
                if map[e] == i:
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        