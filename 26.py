class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        duplicate=set()
        for i in range(n):
            if nums[i] in duplicate:
                nums[i]="#"
            else:
                duplicate.add(nums[i])
        for i in range(len(nums)-1,-1,-1):
            if nums[i]=="#":
                nums.pop(i)
        return len(nums)
        # When you remove an element while iterating backward, the indices of the elements you have yet to visit (which are at lower indices) remain unchanged. This guarantees that you will visit every element exactly once and also dont skip elements as in the case of forward iteration
