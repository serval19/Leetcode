class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums.reverse()
        nums[:k]=list(reversed(nums[:k]))
        nums[k:n]=list(reversed(nums[k:n]))


            
