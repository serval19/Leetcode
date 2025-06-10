class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=defaultdict(int)
        for c in s:
            count[c]=count[c]+1
        for index,c in enumerate(s):
            if count[c]==1:
                return index
        return -1
        
