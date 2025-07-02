class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest=""
        lenlongest=0
        for i in range(len(s)):
            #odd inside out palindrome
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:

                if (r-l+1)> lenlongest:
                    longest=s[l:r+1]
                    lenlongest=r-l+1
                l-=1
                r+=1
            # even sized inside out palindromes
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:

                if (r-l+1)> lenlongest:
                    longest=s[l:r+1]
                    lenlongest=r-l+1
                l-=1
                r+=1
        return longest
