class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n=len(heights)
        stack=[]
        result=[0]*n
        for i in range(n-1,-1,-1):
            count=0
            while stack and stack[-1]<heights[i]:
                stack.pop()
                count+=1
            if stack:
                count+=1
            stack.append(heights[i])
            result[i]=count
        return result
        
        
