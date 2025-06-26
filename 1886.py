class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        l=len(mat)
        if mat==target:
            return True
        for i in range(3):
            mat.reverse()
            for j in range(l):
                for k in range(j+1,l):
                    mat[j][k],mat[k][j]=mat[k][j],mat[j][k]
            if mat==target:
                return True
        return False
