class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols=len(matrix),len(matrix[0])
        index=-1
        for i in range(0,rows):
            if matrix[i][-1]>=target:
                index=i
                break
        if index!=-1:
            for i in range(0,cols):
                if matrix[index][i]==target:
                    return True
        return False
        
