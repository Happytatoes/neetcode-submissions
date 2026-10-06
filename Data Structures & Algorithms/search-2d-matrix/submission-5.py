class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        top_row, bottom_row = 0, rows - 1
        left_col, right_col = 0, cols - 1
        
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if target > matrix[middle_row][-1]:
                top_row = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom_row = middle_row - 1
            else:
        
                while left_col <= right_col:
                    middle_col = (left_col + right_col) // 2
                    if matrix[middle_row][middle_col] == target:
                        return True
                    elif matrix[middle_row][middle_col] < target:
                        left_col = middle_col + 1
                    else:
                        right_col = middle_col - 1
                # found a valid row, but failed within that row
                return False 

        # failed to find valid row
        return False 