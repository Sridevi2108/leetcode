class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution=Solution()
    result=solution.spiralOrder(matrix)
    print(result)



