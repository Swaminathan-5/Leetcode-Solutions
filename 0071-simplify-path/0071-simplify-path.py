class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        slash = path.split('/')
        for i in slash:
            if i == '' or i == '.':
                continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
        