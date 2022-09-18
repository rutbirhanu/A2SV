from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top=left=0
        bottom=len(matrix)
        right=len(matrix[0])
        while top<bottom and left<right:
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            if not (top<bottom and left<right):
                break
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+= 1
        return res
