class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m=len(needle)
        n=len(haystack)
        for i in range(0,n-m+1):
            if haystack[i:i+m]==needle:
                return i
        else:
            return -1
            
        
