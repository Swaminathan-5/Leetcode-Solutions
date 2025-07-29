class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for i in string:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        return build(s) == build(t)