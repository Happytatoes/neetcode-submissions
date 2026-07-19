class Solution:
    
    def rowsValid(self, board: List[List[str]]) -> bool:
        for row in board:
            # rowstorage stores [1-9], 
            # false if that number has appeared,
            # true if it has. 
            # if one is true and we do it again, the row isnt valid
            rowstorage = [False] * 9
            for element in row:
                if element != ".":
                    index_in_rowstorage = int(element) - 1
                    if rowstorage[index_in_rowstorage]:
                        # the element is already there! 
                        # that means there is a duplicate
                        return False
                    else: 
                        rowstorage[index_in_rowstorage] = True
        return True

    def colsValid(self, board: List[List[str]]) -> bool:
        for col in range(0, 9):
            # colstorage stores [1-9], 
            # false if that number has appeared,
            # true if it has. 
            # if one is true and we do it again, the col isnt valid
            colstorage = [False] * 9
            for row in range(0, 9):
                element = board[row][col]
                if element != ".":
                    index_in_colstorage = int(element) - 1
                    if colstorage[index_in_colstorage]:
                        # the element is already there! 
                        # that means there is a duplicate
                        return False
                    else: 
                        colstorage[index_in_colstorage] = True
        return True

    def squaresValid(self, board: List[List[str]]) -> bool:
        # key is square index ((row / 3) * 3 + (col / 3)), value is set of what is already there
        hashy = {}
        # init all hashy to an empty set
        for i in range(0, 9):
            hashy[i] = set()
        
        for row in range(0, 9):
            for col in range (0, 9):
                element = board[row][col]
                if element != ".":
                    index = (row // 3) * 3 + (col // 3)
                    if element in hashy[index]:
                        return False
                    else: 
                        hashy[index].add(element)
        
        return True
                            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.squaresValid(board) and self.colsValid(board) and self.rowsValid(board)




