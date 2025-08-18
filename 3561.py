class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        
        for i in s:
            if stack and i=="a" and stack[-1]=="z":
                stack.pop()
            elif  stack and i=="z" and stack[-1]=="a":
                stack.pop()
            elif (stack and ord(i)+1==ord(stack[-1])) or (stack and ord(i)-1==ord(stack[-1])):
                stack.pop()
            else:
                stack.append(i)
            str=""
        for i in stack:
            str=str+i
        return str
        
