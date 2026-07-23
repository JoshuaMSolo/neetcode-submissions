class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for c in s :
            if c == "(" :
                stack.append(")")
            elif c == "{" :
                stack.append("}")
            elif c == "[" :
                stack.append("]")
            else :
                if not stack or c != stack.pop():
                    return False
        if stack :
            return False
        return True
                
        