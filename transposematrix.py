class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:  
        rows=len(matrix)
        column=len(matrix[0])
        transposematrix=[]
        for i in range(column):
            temp=[]
            for j in range(rows):
                temp.append(matrix[j][i])
            transposematrix.append(temp)

        return transposematrix

        
