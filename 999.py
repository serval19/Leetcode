class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row,col=0,0
        for i in range(len(board)):
            if "R" in board[i]:
                row=i
                matrix=board[i]
                col=matrix.index("R")
        captures=0
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            r,c=row,col
            while True:
                r+=dr
                c+=dc
                if r<0 or r>=8 or c<0 or c>=8:
                    break
                if board[r][c]=="B":
                    break
                if board[r][c]=="p":
                    captures+=1
                    break

        return captures
