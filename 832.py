class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i].reverse()
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image
            
            
        
