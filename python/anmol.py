
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    row_hash_arr = []
    column_hash_arr = []
    box_hash_arr = []
    i = 0
    j = 0
    print(i, j)
    while i < 9:
        print(i, j)
        row_hash = set()
        j = 0
        while j < 9:
            print(i,j)
            if board[i][j] == ".":
                j += 1
                continue
            if board[i][j] in row_hash:
                return False
            else:
                row_hash.add(board[i][j])
            if j >= len(column_hash_arr):
                column_hash_arr.append(set(board[i][j]))
            else:
                if board[i][j] in column_hash_arr[j]:
                    return False
                else:
                    column_hash_arr[j].add(board[i][j])
            j += 1
        i += 1
    print(column_hash_arr)
isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])