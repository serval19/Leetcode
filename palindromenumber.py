class Solution:
    def isPalindrome(self, x: int) -> bool:
        numstr=str(x)
        revnum=numstr[::-1]
        if numstr==revnum:
            return True
        else:
            return False
