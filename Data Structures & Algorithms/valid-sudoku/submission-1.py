class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_dict = {} # key: row number, value: set()
        col_dict = {}
        square_dict = {} # square_index = (row // 3) * 3 + (col // 3)

        for row in range(0, 9):
            for col in range(0, 9):
                
                number = board[row][col]

                if number != '.':

                    if row not in row_dict:
                        row_dict[row] = set()
                        row_dict[row].add(number)
                    else:
                        if number in row_dict[row]:
                            return False
                        else:
                            row_dict[row].add(number)
                    
                    if col not in col_dict:
                        col_dict[col] = set()
                        col_dict[col].add(number)
                    else:
                        if number in col_dict[col]:
                            return False
                        else:
                            col_dict[col].add(number)

                    square_index = (row // 3) * 3 + (col // 3)

                    if square_index not in square_dict:
                        square_dict[square_index] = set()
                        square_dict[square_index].add(number)
                    else:
                        if number in square_dict[square_index]:
                            return False
                        else:
                            square_dict[square_index].add(number)

        return True










