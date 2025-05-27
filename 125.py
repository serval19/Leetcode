class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr=""
        for i in s:
            if i.isalnum():
                newstr=newstr+i.lower()
        return newstr==newstr[::-1]

                
