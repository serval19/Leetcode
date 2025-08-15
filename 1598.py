class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack=[]
        for i in logs:
            if i!="../" and i!="./":
                stack.append(i)
            elif i=="../" and stack:
                stack.pop()
            elif i=="./":
                continue
        return len(stack)
        
