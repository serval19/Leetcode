class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in nums:
            digits=0
            rem=i

            while rem!=0:
                rem=rem//10
                digits+=1
            if digits%2==0:
                count+=1
        return count

        
