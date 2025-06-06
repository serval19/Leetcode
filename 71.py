class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        curr = ""
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: 
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)
