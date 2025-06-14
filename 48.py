class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #first reverse rows from top to bottom and take transpose for clockwise #rotation
        matrix.reverse()
        rows=len(matrix)
        cols=rows
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
