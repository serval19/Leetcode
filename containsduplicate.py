class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1=set(nums)
        if len(set1)==len(nums):
            return False
        else:
            return True